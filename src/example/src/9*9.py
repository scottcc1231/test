#!/usr/bin/env python
import rospy
import sys
print(sys.version)
for i in range(1,10):
    print()
    for j in range(1,10):
        print('%d*%d=%d '%(i,j,i*j),end='')
