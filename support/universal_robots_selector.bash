#!/bin/bash

PS3='Please enter your operating mode: '
options=("With fysical Universal Robots UR5(Wifi mode)" "Without fysical Universal Robots UR5(simulation Mode)" "None")
select opt in "${options[@]}"
do
    case $opt in
        "With fysical Universal Robots UR5(Wifi mode)")
            echo "you chose With fysical Universal Robots UR5(Wifi mode)"
            source $HOME/universal_robots_ws/src/my_universal_robots/support/wifi_network.bash
	    break
            ;;
        "Without fysical Universal Robots UR5(simulation Mode)")
            echo "you chose Without fysical Universal Robots UR5(simulation Mode)"
            source $HOME/universal_robots_ws/src/my_universal_robots/support/simulation.bash
	    break
            ;;
        "None")
            echo "you chose None"
	    break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
