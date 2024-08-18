# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:05:06 2024

@author: Student
"""

a = float(input("do dai canh a la"))
b = float(input("do dai canh b la"))
c = float(input('do dai canh c la'))
if (a+b>c) and (a+c>b) and (b+c>a):
    print(" 3 so nguyen la do dai 3 canh cua tam giac")
else:
    print("3 so nguyen khong la do dai 3 canh cua tam giac")