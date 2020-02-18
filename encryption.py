# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:30:23 2019

@author: Talib
"""
def encryption(s):
    l = len(s)
    row = (l**0.5)
    if(row>int(l**0.5)):
        row = int(l**0.5)
        column = row+1
    else:
        row = column = int(l**0.5)
        
    if(row*column<l):
        row +=1
        
   
    r = column
    
    final = []
    i=0
    while(i<r):
        res = []
        for j in range(l):
            if(j % r ==  i):
                res.append(s[j])
        final.append(''.join(res))
        i+=1
        
    for i in final:
        print(i,end = " ")

