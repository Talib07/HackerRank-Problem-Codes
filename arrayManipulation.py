# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:00:02 2019

@author: Talib
"""

def arrayManipulation(n, queries):
    a=[0]*(n+1)

    for i in range(len(queries)):
        a[queries[i][0]-1] += queries[i][2]
        a[queries[i][1]] += -(queries[i][2])
    
    for i in range(1,n+1):
        a[i] = max(sum(a[i-1 : i+1]),a[i])

    return max(a)