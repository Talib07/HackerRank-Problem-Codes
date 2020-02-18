# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:04:00 2019

@author: Talib
"""

def dooropen(n):
    door = [0]*n
    for i in range(1,n+1):
        for j in range(1,i+1):
            if(i%j==0):
                if(door[i-1]==0):
                    door[i-1]=1
                elif(door[i-1]==1):
                    door[i-1]=0
            
    return door
                    