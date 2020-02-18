# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:40:30 2019

@author: Talib
"""
def flatlandSpaceStations(n, c):
    cities = []
    for i in range(0,n,1):
        cities.append(i)
    #print(cities)
     
    dist = []
    city = []
    distmin = []
    
    if(n==len(c)):
        dist = 0
        
    else:
        i=0
        while cities[i] not in c:
            city.append(cities[i])
            i+=1
                
        for i in city :
            for j in c:
                dist.append(abs(i-j))
            distmin.append(min(dist))
            dist=[]
    
    #print(city)
    #print(c)        
        distance= max(distmin)
        
    return distance