# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:27:25 2019

@author: Talib
"""

def commonfac(a,b):
    count = 0
    #ar = []
    for i in range(1, min(a, b)+1): 
        if (a%i==b%i==0):
      #      ar.append(i)
            count+=1
    
    print(count)    
    return count