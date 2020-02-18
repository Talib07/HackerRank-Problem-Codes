# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:58:18 2019

@author: Talib
"""

def simplesieve(limit):
    a = limit*[1]
    for i in range(2,int(limit**0.5)+1):
        if(a[i]==1):
            for j in range(2*i,limit,i):
                a[j]=0
    
    for i in range(2,limit):
        if(a[i]==1):
            print(i)