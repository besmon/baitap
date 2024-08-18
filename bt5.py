# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:13:32 2024

@author: Student
"""

a = float(input("nhap do dai canh a"))
b = float(input("nhap do dai canh b"))
c = float(input("nhap do dai canh c"))
if (a+b>c) and (a+c>b) and (b+c>a): 
 if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print(" a,b,c la 3 canh cua tam giac vuong")
 elif a==b==c:
     print("a,b,c la 3 canh cua tam giac deu")
 elif a==b or b==c or c==a:
     print(" a,b,c la 3 canh cua tam giac can")
 else: print("a,b,c la 3 canh cua tam giac thuong")