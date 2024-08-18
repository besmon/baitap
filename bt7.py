# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:33:52 2024

@author: ASUS
"""

print("kiểm tra tính hơp lệ của ngày tháng năm")
y = float(input("nhập năm:"))
m = float(input("nhập tháng:"))
if m<1 and m>12:
    print("không hợp lệ")
d = float(input("nhập ngày:"))
if d<1 and d>31:
    print("không hợp lệ")
if y%4==0 and y%100!=0 or y%400 ==0:
    print("nay là năm nhuận")
    if m==2:
        print("tháng này co 29 ngày")
        if d>29:
            print("không hợp lệ")
else:
    print("Năm này không là năm nhuận")
    if m==2:
        print("Tháng này có 28 ngày")
        if d>28:
            print("không hợp lệ")
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print("Tháng này có 31 ngày")
    elif m==2 or m==4 or m==6 or m==9 or m==11:
        print("tháng này có 30 ngày")
        if d>30:
            print("không hợp lệ")
            