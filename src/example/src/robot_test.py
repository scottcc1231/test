#!/usr/bin/env python
import rospy
def Forward(start,right,left,now):
    forward={'Right':right,'Left':left,'Now':now}
    if start: 
        if forward['Now']<forward['Right']:
            move='turn right'
        elif forward['Now']>forward['Left']:
            move='turn left'
        else:
            move='forward'
    else:
        move='error'   
    return move
turn_right=20
turn_left=70
start=int(input("enter true or false="))
turn_now=int(input("enter number="))
print(Forward(start,turn_right,turn_left,turn_now))
