#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
rospy.loginfo("user=iclab_xiao_ming")
password=input("password=")
if password==11:
   print("sucess")
else:
   print("fail")

