# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/wasp_mini/ros2_ws/build/nav2_voxel_grid

# Include any dependencies generated for this target.
include test/CMakeFiles/voxel_grid_tests.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/voxel_grid_tests.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/voxel_grid_tests.dir/flags.make

test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o: test/CMakeFiles/voxel_grid_tests.dir/flags.make
test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o: /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid/test/voxel_grid_tests.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wasp_mini/ros2_ws/build/nav2_voxel_grid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o"
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o -c /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid/test/voxel_grid_tests.cpp

test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.i"
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid/test/voxel_grid_tests.cpp > CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.i

test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.s"
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid/test/voxel_grid_tests.cpp -o CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.s

# Object files for target voxel_grid_tests
voxel_grid_tests_OBJECTS = \
"CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o"

# External object files for target voxel_grid_tests
voxel_grid_tests_EXTERNAL_OBJECTS =

test/voxel_grid_tests: test/CMakeFiles/voxel_grid_tests.dir/voxel_grid_tests.cpp.o
test/voxel_grid_tests: test/CMakeFiles/voxel_grid_tests.dir/build.make
test/voxel_grid_tests: gtest/libgtest_main.a
test/voxel_grid_tests: gtest/libgtest.a
test/voxel_grid_tests: libvoxel_grid.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librclcpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector_test_msgs__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/liblibstatistics_collector_test_msgs__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstd_msgs__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstd_msgs__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstd_msgs__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstd_msgs__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstd_msgs__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_interfaces__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_interfaces__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_interfaces__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_interfaces__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_interfaces__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librmw_implementation.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librmw.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_logging_spdlog.so
test/voxel_grid_tests: /usr/lib/x86_64-linux-gnu/libspdlog.so.1.5.0
test/voxel_grid_tests: /opt/ros/foxy/lib/librcl_yaml_param_parser.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libyaml.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosgraph_msgs__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosgraph_msgs__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosgraph_msgs__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosgraph_msgs__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosgraph_msgs__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstatistics_msgs__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstatistics_msgs__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstatistics_msgs__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstatistics_msgs__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libstatistics_msgs__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libbuiltin_interfaces__rosidl_generator_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libbuiltin_interfaces__rosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosidl_typesupport_introspection_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosidl_typesupport_introspection_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libbuiltin_interfaces__rosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosidl_typesupport_cpp.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosidl_typesupport_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcpputils.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librosidl_runtime_c.so
test/voxel_grid_tests: /opt/ros/foxy/lib/librcutils.so
test/voxel_grid_tests: /opt/ros/foxy/lib/libtracetools.so
test/voxel_grid_tests: test/CMakeFiles/voxel_grid_tests.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wasp_mini/ros2_ws/build/nav2_voxel_grid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable voxel_grid_tests"
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/voxel_grid_tests.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/voxel_grid_tests.dir/build: test/voxel_grid_tests

.PHONY : test/CMakeFiles/voxel_grid_tests.dir/build

test/CMakeFiles/voxel_grid_tests.dir/clean:
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test && $(CMAKE_COMMAND) -P CMakeFiles/voxel_grid_tests.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/voxel_grid_tests.dir/clean

test/CMakeFiles/voxel_grid_tests.dir/depend:
	cd /home/wasp_mini/ros2_ws/build/nav2_voxel_grid && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid /home/wasp_mini/ros2_ws/src/navigation2/nav2_voxel_grid/test /home/wasp_mini/ros2_ws/build/nav2_voxel_grid /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test /home/wasp_mini/ros2_ws/build/nav2_voxel_grid/test/CMakeFiles/voxel_grid_tests.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/voxel_grid_tests.dir/depend

