cmake_minimum_required(VERSION 3.5)
project(main_waspmini)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

add_executable(joy_pub src/joy_pub.cpp)
ament_target_dependencies(joy_pub rclcpp std_msgs sensor_msgs)
ament_python_install_package(${PROJECT_NAME})

install(TARGETS 
joy_pub
DESTINATION lib/${PROJECT_NAME}/)

install(DIRECTORY
launch
DESTINATION share/${PROJECT_NAME}/
)

# Install Python executables
install(PROGRAMS
  scripts/motor_FR.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/motor_FL.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/actuator_fb.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/main.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
