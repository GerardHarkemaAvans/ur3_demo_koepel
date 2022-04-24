#!/bin/bash

#cd $HOME/universal_robots_ws/src
cd ../..

git clone -b boost https://github.com/UniversalRobots/Universal_Robots_Client_Library.git
git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git
git clone -b calibration_devel https://github.com/fmauch/universal_robot.git
git clone https://github.com/ros-industrial/ur_msgs.git

sudo apt update -qq
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -y

catkin b

