#!/usr/bin/env python
import rospy
def welcome(name,when):
    print('HI,',name,',Good',when)

welcome(name='scott',when='Morning')

def sub(x1,x2):
    return x1-x2
def add(x1,x2):
    return x1+x2
op=int(input('choose funtion enter 1 or 2='))
a=int(input('a='))
b=int(input('b='))
if op==1:
    print('a+b=',add(a,b))
elif op==2:
    print('a-b=',sub(a,b))
else:
    print('error')

def list_num(num):
    for i in range(len(num)):
        num[i]=num[i]+30
number=[0,20,40]
list_num(number)
print(number)

def build_member(name,gender,tel):
    member={'Name':name,'Gender':gender,'Tel':tel}
    if tel:
        member['tel']=tel
    return member
member_name=input('name:')
member_gender=input('gneder:')
member_tel=input('tel:')
print(build_member(member_name,member_gender,member_tel))
