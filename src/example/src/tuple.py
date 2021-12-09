#!/usr/bin/env python
import rospy
a='t','u','p','l','e'
b=tuple(a)
print(b)


tuple1=('Red','Green','Blue')
(R,G,B)=tuple1
print(R)
print(G)
print(B)


dict_example={'a':'apple','b':'banana','c':'cat'}
print(dict_example)
list1=[['math','100'],['english','98']]
x=dict(list1)
print(x)


x=('key1','key2','key3')
y=1
keydict=dict.fromkeys(x,y)
print(keydict)


Gender={'men':'a','women':'b'}
print(Gender)
Gender['?']='me'
print(Gender)
Gender.update({'!':'you'})
print(Gender)


print(Gender['men'])
print(Gender.get('women'))


fruit={'red':'apple','purple':'grape','orange':'orange'}
print(fruit)
fruit.pop('red')
print(fruit)

fruit={'red':'apple','purple':'grape','orange':'orange'}
print(fruit)
fruit.clear()
print(fruit)

