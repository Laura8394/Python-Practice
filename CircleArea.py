# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:11:04 2018

@author: laura
"""
import math

r = int(input("Enter the radius: "))
s = math.pi * r ** 2
f = math.pi * r * 2
print("The CircleFerence Is: {: .10f}".format(f))
print("The CircleArea Is: {: .10f}".format(s))

a = float(input("Enter the length: "))
l = a * 4
print("The Square CircumFerence Is {:5.2f}m".format(l))
