# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:58:30 2020

@author: USER
"""

score = int(input("please enter your score:"))

if score >= 0 and score <=100:
    if score >= 90:
        print("level A")
    elif score >= 80:
        print("level B")
    elif score >= 70:
        print("level C")
    elif score >= 60:
        print("level d")
    else:
        print("level E")
        
else:
    print("thats's wrong")