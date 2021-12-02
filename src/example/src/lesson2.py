#!/usr/bin/env python
import rospy
rospy.init_node("lesson2")
num=[]
for i in range(1,11,2):
    a=[i]
    num=num+a
print(num)
print(max(num))
print(min(num))
print(sum(num))


