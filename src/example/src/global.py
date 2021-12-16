#!/usr/bin/env python
import rospy
def increase():
    global x
    x+=1
x=1
print(x)
increase()
print(x)
