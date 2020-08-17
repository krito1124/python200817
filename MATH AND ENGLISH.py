# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:38:04 2020

@author: USER
"""

mathscore = int(input("what is your math score?:"))
englishscore = int(input("what is your  english score?:"))

if mathscore >= 0 and mathscore <=100 and englishscore >= 0 and englishscore <=100:
    if mathscore >=90 and englishscore >=90:
        print("you will have a prize")
    elif mathscore <60 and englishscore <60:
        print("you will be punish")
    elif  mathscore  or englishscore <60:
        print("再加油")
else:
    print("that's wrong")
    


