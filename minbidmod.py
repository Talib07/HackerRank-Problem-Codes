# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:43:46 2019

@author: Talib
"""

l = list( input().split() )

d= {}

final = []

for i in range(10):
    d[str(i)] = i
    
S = "ABCDEFGHIJKLMNOPQRSTUBWXYZ"

x= 10
for i in S:
    d[i] = x
    x+=1
    
l=['1Z','A','L0','35']

for i in l:
    temp = -1
    for j in i:
        temp = max(temp,d.get(j))
    base = temp + 1
    
    lst = []
    for j in i:
        lst.append(d.get(j))   
    lst.reverse()
    
    decimalno = 0
    power = 0
    
    for i in lst:
        decimalno += i*(base**power)
        power+=1
    
    print(decimalno)
    final.append(decimalno)
    
print(min(final))
    
        
        

    