# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:42:53 2019

@author: Talib
"""
import math
MOD = 1000000007

def Mystery(n,a,q,l,r):
    if(l==r):
        res = 1
    
    
    
        prod = 1
        
        for i in range(l-1,r,1):
            prod = prod * math.factorial(a[i])
        prod = prod % MOD
        prod = prod ** (r-l)
        res = prod
        
        return res
    