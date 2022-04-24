#!/bin/bash

PS3='Please enter your operating mode: '
options=("With fysical Niryo Ned Robot(Hotspot mode)" "With fysical Niryo Ned Robot(Wifi mode)" "None")
select opt in "${options[@]}"
do
    case $opt in
        "With fysical Niryo Ned Robot(Hotspot mode)")
            echo "you chose With fysical Niryo Ned Robot(Hotspot mode)"
            source $HOME/niryo_ned_support/environment/hotspot_network.bash
            roslaunch my_niryo_robot_hardware_interface hardware_interface_standalone.launch
	    break
            ;;
        "With fysical Niryo Ned Robot(Wifi mode)")
            echo "you chose With fysical Niryo Ned Robot(Wifi mode)"
            source $HOME/niryo_ned_support/environment/wifi_network.bash
            roslaunch my_niryo_robot_hardware_interface hardware_interface_standalone.launch
	    break
            ;;
        "None")
            echo "you chose Without fysical Niryo Ned Robot"
	    break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
