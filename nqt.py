# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:31:05 2019

@author: Talib
"""

word = input()

inp = ["for","defer","else","func","for","if","range","print","int"]

if(word in inp):
    print(str(word)+" is a keyword")
else:
    print(str(word)+" is not a keyword")