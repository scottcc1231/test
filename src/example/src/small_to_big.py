#!/usr/bin/env python
import rospy
num=[]
for i in range(3):
    x=int(input('enter number='))
    num.append(x)
num.sort()
print(num)



