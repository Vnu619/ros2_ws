#include "rclcpp/rclcpp.hpp"
#include <sensor_msgs/msg/joy.hpp>
#include <geometry_msgs/msg/twist.hpp>
class JoyPublisherNode: public rclcpp::Node{
    public:
        JoyPublisherNode(): Node("Joy_Publisher")
        {
            joy_subscriber = this->create_subscription<sensor_msgs::msg::Joy>("joy", 10, std::bind(&JoyPublisherNode::PublishCmdvel, this, std::placeholders::_1));
            cmd_publisher = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
            timer_ = this->create_wall_timer(std::chrono::seconds(1),std::bind(&JoyPublisherNode::callBack, this));
            RCLCPP_INFO(this->get_logger(), "ros2 in cpp");
        }

    private:
        rclcpp::Subscription<sensor_msgs::msg::Joy>::SharedPtr joy_subscriber;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_publisher;
        rclcpp::TimerBase::SharedPtr timer_;
        void callBack()
        {
            RCLCPP_INFO(this->get_logger(), "ros2 in cpp");
        }
        void PublishCmdvel(const sensor_msgs::msg::Joy::SharedPtr joy)
        {
            RCLCPP_INFO(this->get_logger(), "hi_subscribing joy_msgs");
            auto command_velocity = geometry_msgs::msg::Twist();
            command_velocity.linear.x = 0.1*joy->axes[1];
            command_velocity.angular.z = 1*joy->axes[0];
            command_velocity.angular.x = 0.1*joy->axes[5];
            command_velocity.angular.y = 0.1*joy->buttons[3];
            cmd_publisher->publish(command_velocity);
        }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<JoyPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}