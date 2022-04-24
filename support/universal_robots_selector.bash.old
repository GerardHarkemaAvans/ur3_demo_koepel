#!/bin/bash

PS3='Please enter your operating mode: '
options=("With fysical Niryo Ned Robot(Hotspot mode)" "With fysical Niryo Ned Robot(Wifi mode)" "With fysical Niryo Ned Robot(Ethernet mode)" "Without fysical Niryo Ned Robot (simulation Mode)" "None")
select opt in "${options[@]}"
do
    case $opt in
        "With fysical Niryo Ned Robot(Hotspot mode)")
            echo "you chose With fysical Niryo Ned Robot(Hotspot mode)"
            source $HOME/niryo_robot_ws/src/my_niryo_robot/support/hotspot_network.bash
	    break
            ;;
        "With fysical Niryo Ned Robot(Wifi mode)")
            echo "you chose With fysical Niryo Ned Robot(Wifi mode)"
            source $HOME/niryo_robot_ws/src/my_niryo_robot/support/wifi_network.bash
	    break
            ;;
        "With fysical Niryo Ned Robot(Ethetnet mode)")
            echo "you chose With fysical Niryo Ned Robot(Ethernet mode)"
            source $HOME/niryo_robot_ws/src/my_niryo_robot/support/ethernet_network.bash
	    break
            ;;
        "Without fysical Niryo Ned Robot (simulation Mode)")
            echo "you chose Without fysical Niryo Ned Robot (simulation Mode)"
            source $HOME/niryo_robot_ws/src/my_niryo_robot/support/simulation.bash
	    break
            ;;
        "None")
            echo "you chose None"
	    break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
