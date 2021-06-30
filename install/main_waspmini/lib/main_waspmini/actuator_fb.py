#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
#from roboclaw import Roboclaw as RB
import wasp_mini_controller.roboclaw_3 as RB

#rc = RB.Roboclaw("/dev/ttyACM0",115200)
#rc.Open()
#print(rc.ReadEncM1(0x80)[1])
class PublishFeedback(Node):
    def __init__(self):
        super().__init__("actuator_position")
        self.publisher_ = self.create_publisher(Int32, "/post", 10)
        self.pub_timer = self.create_timer(0.1, self.publish_position)
        self.address = 0x80
        self.rc = RB.Roboclaw("/dev/ttyACM0",115200)
        self.rc.Open()

    def publish_position(self):
        position_read = Int32()
        position_read.data = self.rc.ReadEncM1(self.address)[1]
        self.publisher_.publish(position_read)

def main(args = None):
    rclpy.init(args=args)
    node = PublishFeedback()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
