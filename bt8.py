# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:23:13 2024

@author: Student
"""

nguoichoi = float(input("nguoi chon (1.keo, 2.bua, 3.bao):"))
from random import randint
maychon = randint(1,3)
if maychon==1:
    print("may chon: keo")
elif maychon==2:
    print("may chon bua")
elif maychon==3:
    print("may chon bao")
if maychon==nguoichoi:
    print("hoa nhau")
elif maychon==1 and nguoichoi ==2 or maychon ==2 and nguoichoi ==3 or maychon ==3 and nguoichoi ==1:
    print("nguoi choi thang")
else: print("may thang")