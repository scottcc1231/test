#!/usr/bin/env python
import rospy
import random
x=3
num=[[[None for k in range(x)]for j in range(x)]for i in range(x)]
result=[[[None for k in range(x)]for j in range(x)]for i in range(x)]
for i in range(x):
    for j in range(x):
        for k in range(x):
            a=random.randint(0,255)
            num[i][j][k]=a
            if a<125:
                result[i][j][k]=0
            else:
                result[i][j][k]=1
print(num)
print(result)
                
