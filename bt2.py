# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:16:21 2024

@author: Student
"""

a = float(input("nhap a"))
b = float(input("nhap b"))
if a == 0 and b!=0:
    print("phuong trinh vo nghiem")
elif a==0 and b==0:
    print("phuong trinh co vo so nghiem")
else:
    print("nghiem cua phuong trinh la:", -b/a)