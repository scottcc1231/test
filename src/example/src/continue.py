#!/usr/bin/env python
import rospy
s="Hello World"
for S in s:
    if S=="o":
        continue
    print(S)
