# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:15:02 2019

@author: Talib
"""
from itertools import permutations

def exchange(a,b):
    small = min(a,b)
    small = str(small)
    l = list(map(int,small))
    print(l)
    k = permutations(l)
    w = [[str(x) for x in tup] for tup in k]
    ll = []
    for i in w:
        ll.append(int("".join(i)))
    ff = sorted(i for i in ll if i > b)
    
    if(len(ff)>0):
        res = min(ff)
    else:
        res = -1
    
    return res
    
        
exchange(459,500)