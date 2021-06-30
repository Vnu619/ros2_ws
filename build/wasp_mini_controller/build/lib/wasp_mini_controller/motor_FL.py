#!/usr/bin/env python3
import wasp_mini_controller.orienbus as orienbus
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import *

address = 2
port = '/dev/wasp_motorFL'

orienbus = orienbus.OrienBus(port)
#motor = orienbus.initialize(address)

class PubSubMotor(Node):
    def __init__(self):
        super().__init__("motor_FL")
        self.get_logger().info("ros2")
        self.speed=0
        self.motor = orienbus.initialize(address)
        #speed_read = self.motor.readSpeed()
        #
        self.subscriber_= self.create_subscription(Twist,"target_speed",self.callback,1)
        self.publisher_ = self.create_publisher(Int32, "/speed_fl", 1)
        self.pub_timer = self.create_timer(0.1, self.publish_speed)

    def publish_speed(self):

        speed_read = Int32()
        self.get_logger().info("hello")
        speed_read.data = self.motor.readSpeed()
        print(speed_read.data)
        self.publisher_.publish(speed_read)

    def callback(self, data):
        self.speed = data.linear.x
        self.motor.writeSpeed(self.speed)

        #self.get_logger().info("ros2___")

def main(args=None):
    rclpy.init(args=args)
    node  = PubSubMotor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
