# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:46:01 2019

@author: Talib
"""

def twoStrings(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if(l1>l2):
        st = s1
        st2 = s2
    else:
        st = s2
        st2 = s1
    
    d={}
    
    for i in st:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    counter = 0   
    print(d)    
    
    for i in st2:
        if (i not in d.keys()):
            print(i)
            print("Not Present")
            counter += 0
            print(counter)
        else:
            print(i)
            print("Present")
            counter += 1
            print(counter)
            
    print(counter)
    if(counter==0):
        print("No")
    else:
        print("Yes")
            
twoStrings("aardvark","apple")        