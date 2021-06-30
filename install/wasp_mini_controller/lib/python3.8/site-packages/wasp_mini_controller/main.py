#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
import time
from rclpy.time import Time
import math
import tf2_ros
import numpy as np
#import tf2_geometry_msgs
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Quaternion
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import *
import wasp_mini_controller.roboclaw_3 as RB

xdot = 0
thetadot = 0
R = 0.100   # Wheel radius 100mm
B = 0.345   # Distance between wheels 345mm
L = 0.300
#timer = Time.Second()
class WaspMiniController(Node):
    def __init__(self):
        super().__init__("main")
        self.rc = RB.Roboclaw("/dev/ttyACM0",115200)
        self.rc.Open()
        self.address = 0x80
        self.upper_limit = 1180
        self.lower_limit = 80
        self.upper_position = 1080
        self.lower_position = 180
        self.initial_position = 250

        # Define kinematics parameters
  # The length of the robot base 300mm
        self.loop_rate = 5
        self.flag = 0
        self.target_speed_pub = self.create_publisher(Twist, "/target_speed", 10)
        self.wheel_odom_pub = self.create_publisher(Odometry, "/wheel_odom", 10)
        self.subscriber_cmd_vel = self.create_subscription(Twist, "/cmd_vel", self.loop,1)
        self.subscriber_speed_fl = self.create_subscription(Int32, "/speed_fl", self.fl_speed,1)
        self.subscriber_speed_fr = self.create_subscription(Int32, "/speed_fr", self.fr_speed,1)
        self.subscriber_imu = self.create_subscription(Imu, "/vectornav/IMU", self.imucallback,1)
        self.subscriber_post = self.create_subscription(Int32, "/post", self.callback_position_feedback,1)
        #self.pub_timer = self.create_timer(0.1, self.publish_position)

        self.x_ = 0.0
        self.y_ = 0.0
        self.z_ = 0.0
        self.th = 0.0
        self.prev_time = self.get_clock().now()
        self.odomBroadcaster = tf2_ros.TransformBroadcaster(self)
        self.imu_msg = Imu()
        self.gear_ratio = 50
        self.xdot = 0
        self.thetadot = 0
        self.roll = 0
        self.pitch = 0
        self.prev_yaw = 0
        self.imu_flag = 0
        self.fl_msg = 0
        self.fr_msg = 0
        self.velx = 0
        self.vely = 0
        self.key = 0
        self.position = 0
        self.init_button = 0
        #self.initialize()
    def fl_speed(self, msg):
        self.fl_msg = msg.data

    def fr_speed(self, msg):
        self.fr_msg = msg.data

    def initialize(self):
        if self.rc.ReadEncM1(self.address)[1] != self.initial_position:
            if self.rc.ReadEncM1(self.address)[1] < self.initial_position:
                while self.rc.ReadEncM1(self.address)[1] < self.initial_position:
                    self.rc.SpeedM1(self.address, 250)
                    #self.Duration(0.1)
                    self.display()
                else:
                    self.rc.SpeedM1(self.address, 0)
                    #self.Duration(2)
            else:
                while self.rc.ReadEncM1(self.address)[1] > self.initial_position:
                    self.rc.SpeedM1(self.address, -250)
                    #self.Duration(0.1)
                else:
                    self.rc.SpeedM1(self.address, 0)
                    #self.Duration(2)
        else:
            print("The linear actuator is ready!")


    def display(self):
        print("Position = ", self.rc.ReadEncM1(self.address)[1])

    def euler_from_quaternion(self,quaternion_x, quaternion_y, quaternion_z, quaternion_w):
        x = quaternion_x
        y = quaternion_y
        z = quaternion_z
        w = quaternion_w
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw
    def quaternion_from_euler(self,roll, pitch, yaw):
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        q = [0] * 4
        q[0] = cy * cp * cr + sy * sp * sr
        q[1] = cy * cp * sr - sy * sp * cr
        q[2] = sy * cp * sr + cy * sp * cr
        q[3] = sy * cp * cr - cy * sp * sr

        return q
    def imucallback(self, msg):
        self.imu_msg = msg
        if self.imu_flag == 0:
            (self.roll, self.pitch, self.prev_yaw) = self.euler_from_quaternion(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)
            self.imu_flag = 1
    def forwardkinematics(self):
        xdot = self.xdot
        thetadot = self.thetadot
        # Speed unit conversion from m/s to rpm, from cmd_vel to motor driver
        phi_fl = (50 / R) * (xdot + (B / 2) * thetadot) * (60 / (2 * 3.14))
        phi_fr = -(50 / R) * ((xdot) - (B / 2) * thetadot) * (60 / (2 * 3.14))
        # define target_speed
        target_speed = Twist()
        target_speed.linear.x = phi_fl
        target_speed.linear.y = phi_fr
        #target_speed.linear.x = 2500
        #target_speed.linear.y = 2500
        target_speed.angular.y = 0.0
        target_speed.angular.z = 0.0
        self.target_speed_pub.publish(target_speed)
        #define dt
        curr_time = self.get_clock().now()
        dt_ = ((curr_time - self.prev_time))
        print('hi dt=',(dt_.nanoseconds))
        dt = dt_.nanoseconds*0.000000001
        # feedback velocity from motor driver, conversion to m/s
        v_fl_real = (float(self.fl_msg) * ((2 * 3.14) / 60)) * R / 50
        v_fr_real = -(float(self.fr_msg) * ((2 * 3.14) / 60)) * R / 50
        #print(v_fr_real, v_fr_real)
        (r, p, yaw) = self.euler_from_quaternion(self.imu_msg.orientation.x, self.imu_msg.orientation.y, self.imu_msg.orientation.z, self.imu_msg.orientation.w)
        #delta_th = yaw - self.prev_yaw
        self.prev_yaw = yaw
        # robot velocity = 0.5 * (left wheel velocity + right wheel velocity)
        Vx_real = (v_fl_real + v_fr_real) * 0.5
        #thetadot_real = delta_th / dt
        #thetadot_real = 0.5 / (0.3 + B) * (v_fl_real - v_fr_real)
        thetadot_real = (v_fr_real - v_fl_real) / B
        print(Vx_real, thetadot_real)
        delta_x = (Vx_real * math.cos(self.th)) * dt
        delta_y = (Vx_real * math.sin(self.th)) * dt
        delta_th = thetadot_real * dt
        #print(delta_x, delta_y)
        #self.x_ += delta_x
        #self.y_ += delta_y
        #self.th += delta_th
        #vx = Vx_real
        #vth = thetadot_real

        #L_pose = [str(v_fl_real), ",", str(v_fr_real) + "\n"]
        #file1.writelines(L_pose)

        if ((max(v_fl_real, v_fr_real) > 1) or (min(v_fl_real, v_fr_real) < -1)):
            self.x_ += 0.0
            self.y_ += 0.0
            self.th += 0.0
            vx = 0.0
            vth = 0.0
        else:
            self.x_ += delta_x
            self.y_ += delta_y
            self.th += delta_th
            vx = Vx_real
            vth = thetadot_real
        self.velx = vx
        odom_quat = Quaternion()
        odom_quat = self.quaternion_from_euler(0, 0, self.th)
        t = tf2_ros.TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "odom"
        t.child_frame_id = "base_link"
        t.transform.translation.x = self.x_
        t.transform.translation.y = self.y_
        t.transform.translation.z = self.z_
        t.transform.rotation.x = odom_quat[0]
        t.transform.rotation.y = odom_quat[1]
        t.transform.rotation.z = odom_quat[2]
        t.transform.rotation.w = odom_quat[3]
        self.odomBroadcaster.sendTransform(t)

        odom = Odometry()
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'
        odom.header.stamp = self.get_clock().now().to_msg()
        odom.pose.pose.position.x = self.x_
        odom.pose.pose.position.y = self.y_
        odom.pose.pose.position.z = self.z_
        odom.pose.pose.orientation.x = odom_quat[0]
        odom.pose.pose.orientation.y = odom_quat[1]
        odom.pose.pose.orientation.z = odom_quat[2]
        odom.pose.pose.orientation.w = odom_quat[3]
        odom.twist.twist.linear.x = vx
        #odom.twist.twist.linear.y = vy
        odom.twist.twist.angular.z = vth
        self.prev_time = curr_time
        self.wheel_odom_pub.publish(odom)

    def loop(self, msg):
        self.key = msg.angular.x
        self.init_button = msg.angular.y
        self.xdot = msg.linear.x
        #self.ydot = msg.linear.y
        self.thetadot = msg.angular.z
        self.forwardkinematics()
    def callback_position_feedback(self, data):
        self.position = data.data
        if (self.lower_limit < self.position < self.upper_limit) and (self.init_button != 0.1):
            if self.key > 0.0 and (self.lower_limit < self.position < self.upper_position):
                self.rc.SpeedM1(self.address, 250)
#                print("The linear actuator is extruding...")
            elif self.key < 0.0 and (self.lower_position < self.position < self.upper_limit):
                self.rc.SpeedM1(self.address, -250)
#                print("The linear actuator is retracting...")
            elif self.key == 0.0:
                self.rc.SpeedM1(self.address, 0)
#                print("The linear actuator stops.")
            elif self.position < self.lower_position:
                self.rc.SpeedM1(self.address, 0)
#                print("The linear actuator minimum position reached.")
            elif self.position > self.upper_position:
                self.rc.SpeedM1(self.address, 0)
#                print("The linear actuator maximum position reached.")
            elif (self.lower_limit > self.position > self.upper_limit) and (self.init_button != 0.1):
                self.rc.SpeedM1(self.address, 0)
                #self.Duration(2)
#               print("The linear actuator is beyond limit. Initialization needed.")
        elif self.init_button == 0.1:
            self.initialize()

def main(args=None):
    rclpy.init(args=args)
    node  = WaspMiniController()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
