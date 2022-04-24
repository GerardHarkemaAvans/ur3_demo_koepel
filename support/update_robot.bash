#!/bin/bash


cd $HOME/universal_robots_ws/src
echo "Updating urdf of robot..."
sshpass -p ur5 scp -r my_universal_robots/my_ur_description/urdf ur5@$ROS_MASTER:/home/niryo/catkin_ws/src/my_universal_robots/my_ur_description

echo "Updating moveit config of robot..."
sshpass -p ur5 scp -r my_universal_robots/my_ur5_moveit_config/config ur5@$ROS_MASTER:/home/niryo/catkin_ws/src/my_universal_robots/my_ur5_moveit_config

echo "Ready"
