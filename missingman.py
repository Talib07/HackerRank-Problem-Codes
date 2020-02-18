# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:37:30 2019

@author: Talib
"""
import random
result = []

initial = []
l1 = []
l2 = []
l3 = []


for i in range(0,100000):
    initial.append(random.randint(1,523))
    
for i in range(0,99999):
    l1.append(random.randint(1,523))
    
for i in range(0,99998):
    l2.append(random.randint(1,523))
    
for i in range(0,99997):
    l3.append(random.randint(1,523))
    

for i in initial:
    if(i not in l1 or l1.count(i) < initial.count(i)):
        result.append(i)
        break
    
for i in l1:
    if(i not in l2 or l2.count(i) < l1.count(i)):
        result.append(i)
        break
    
for i in l2:
    if(i not in l3 or l3.count(i) < l2.count(i)):
        result.append(i)
        break

for i in result:
    print(i)



