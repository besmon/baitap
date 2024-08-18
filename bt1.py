# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:08:51 2024

@author: Student
"""

distance = float(input("nhap diem trung binh GPA:"))
if distance <3.5:
    print("Hoc luc kem")
elif distance >=3.5 and distance <5.0 :
    print("hoc luc yeu")
elif distance >=5.0 and distance <7.0:
    print("hoc luc trung binh")
elif distance >=7.0 and distance < 8.0:
    print("hoc luc kha")
elif distance >=8.0 and distance < 9.0:
    print("hoc luc gioi")
elif distance >=9.0 and distance<10:
    print("hoc luc xuat xac")