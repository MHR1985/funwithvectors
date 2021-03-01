# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:15:05 2021

@author: Martin Høigaard Cupello
"""

import numpy as np
import math

def mag(vec):
    x = vec[0]
    y= vec[1]
    mag = math.sqrt(x*x+y*y)
    return mag
mag(np.array([2,2]))

def unit(vec):
    x = vec[0]
    y = vec[1]
    unit_x = x/math.sqrt(x**2+y**2)
    unit_y = y/math.sqrt(x**2+y**2)
    array = np.array([unit_x,unit_y])
    return array;  

def rot90(vec):
    x = vec[0]
    y= vec[1] 
    array= np.array([-y,x])
    return array;

rot90([7,2])

a = np.array([3,2])
b = np.array([8,7])
c = np.array([1,5])

print("2*a")
print(2*a)
print()
print("a+b-c")
print(a+b-c)
print()
print("a*a")
print(np.dot(a,a))
print()
print("mag(a)*mag(a)")
print(mag(a)*mag(a))
print()
print("a*b")
print(np.dot(a,b))
print()
print("a*ar")
print(np.dot(a,rot90(a)))
        