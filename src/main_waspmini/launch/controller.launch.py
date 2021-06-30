from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    motor_fl_node= Node(
        package="main_waspmini",
        executable="motor_FL.py"
    )
    motor_fr_node= Node(
        package="main_waspmini",
        executable="motor_FR.py"
    )
    actuator_fb_node= Node(
        package="main_waspmini",
        executable="actuator_fb.py"
    )
    main_node= Node(
        package="main_waspmini",
        executable="main.py"
    )
    joy_pub_node= Node(
        package="main_waspmini",
        executable="joy_pub"
    )
    imu_tf= Node(package = "tf2_ros", 
        executable = "static_transform_publisher",
        arguments = ["0", "0", "0", "0", "0", "0", "base_link", "imu"])

    ld.add_action(motor_fl_node)
    ld.add_action(motor_fr_node)
    ld.add_action(actuator_fb_node)
    ld.add_action(main_node)
    ld.add_action(joy_pub_node)
    ld.add_action(imu_tf)
    return ld
