# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:33:24 2024

@author: Student
"""
discount=0.92
a = float(input("quang duong di duoc (km)"))
if a<=1:
    st=a*20
    print(" so tien phai thanh toan", st)
elif a>1 and a<=3:
    st=a*13
    print(" so tien phai thanh toan", st)
elif a>=4 and a<=8 :
    st=a*12
    print("so tien phai thanh toan", st)
elif a>=8: 
    st=a*10
    print(" so tien phai thanh toan", st)
    if st>=100:
     Tong= st*discount
     print(" Tong so tien phai thanh toan ", Tong)
