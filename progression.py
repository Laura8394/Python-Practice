# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:22:22 2018

@author: laura
"""

# 数列求和 1/x+1/(x+1)+...+1/n, 设x=1,n=10
# 定义数列函数
sum = 0 
for i in range(1, 11):
    sum += 1 / i 
    print("{:2d} {:.4f}".format(i, sum))
    