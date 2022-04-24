#!/bin/bash

cd $HOME/universal_robots_ws/src

#sshpass -p robotics ssh niryo@$ROS_MASTER "mkdir /home/niryo/universal_robots_ws/src/my_universal_robots"


#echo "Uploading  my_universal_robots_hardware_interface files to robot..."
#sshpass -p ur5 scp -r my_universal_robots/my_universal_robots_hardware_interface ur5@$ROS_MASTER:/home/niryo/catkin_ws/src/my_universal_robots

#echo "Uploading  my_universal_robots_description files to robot..."
#sshpass -p ur5 scp -r my_universal_robots/my_universal_robots_description ur5@$ROS_MASTER:/home/niryo/catkin_ws/src/my_universal_robots


#echo "Uploading  my_niryo_ned_moveit_config files to robot..."
#sshpass -p ur5 scp -r my_universal_robots/my_niryo_ned_moveit_config ur5@$ROS_MASTER:/home/niryo/catkin_ws/src/my_universal_robots




#echo "Ready"
#echo 
#echo "Do not forget to build workspace and source it on the robot"
#echo "Commands on the robot terminal:"
#echo "$ cd ~/catkin_ws/"
#echo "$ catkin_make clean" # not always nessery
#echo "$ catkin_make"
#echo "$ source devel/setup.bash"
