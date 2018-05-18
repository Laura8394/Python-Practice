# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:33:14 2018

@author: laura
"""

a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
    