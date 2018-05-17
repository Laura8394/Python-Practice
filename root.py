# -*- coding:utf-8 -*-
"""
Created on Thu May 17 21:37:51 2018

@author: laura
"""

# 求解一元二次方程
# 一元二次方程式： ax**2 + bx + c = 0
# 求根的公式：x = -b +-(((b**2 - 4ac) ** 0.5) / 2a)
a = float(input("Enter The Number Of a: "))
b = float(input("Enter The Number Of b: "))
c = float(input("Enter The Number Of c: "))
d = b ** 2 - 4 * a * c 

if d < 0:
    print("No Root")
else:
    root1 = -b + (((b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    root2 = -b - (((b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    print("Root1 Is: {: .4f}".format(root1))
    print("Root2 Is: {: .4f}".format(root2))