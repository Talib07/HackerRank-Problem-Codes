# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:46:28 2019

@author: Talib
"""

def solve(a, b, x, y):
    if(GCD(a,b)==GCD(x,y)):
        return "YES"
    else:
        return "NO"

def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)