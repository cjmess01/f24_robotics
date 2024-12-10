#!/bin/bash
source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
cd f24_robotics
colcon build
source install/setup.bash
ros2 launch webots_hw5 webots_hw5.launch.py
