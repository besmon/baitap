# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:27:39 2024

@author: Student
"""
import math 
a = float(input("nhap a"))
b = float(input("nhap b"))
c = float(input("nhap c"))
delta =b*b - 4*a*c
if delta<0:
    print("phuong trinh vo nghiem")
elif delta==0:
    print("phuong trinh co nghiem kep x1=x2", -b/(2*a))
else:
    print("phuong trinh co 2 nghiem phan biet")
    print("x1=", (-(b) + math.sqrt (delta))/(2*a))
    print("x2=", (-(b) - math.sqrt (delta))/(2*a))
    