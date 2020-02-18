# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:58:39 2019

@author: Talib
"""
prime = []
def simplesieve(lim):
    a = [1]*lim
    for i in range(2,int(lim**0.5)+1):
        if(a[i]==1):
            for j in range(2*i,lim,i):
                a[j]=0
                
    #for printing all the prime numbers
    for i in range(2,lim):
        if(a[i]==1):
            prime.append(i)

def segmentedsieve(n):
    lim = int(n**0.5)+1
    simplesieve(lim)
    low = lim
    high = 2*low
    
    while low<n:
        if(high>=n):
            high = n
    
    a = [1]*lim
    for i in range(len(prime)):
        lowLim = (low//prime[i])/prime[i]
        if(lowLim<low):
            lowLim += prime[i]
    
        for j in range(lowLim,high,prime[i]):
            a[j-low] = 0
            
    for i in range(low,high):
        if(a[i-low]==1):
            print(i , end = " ")
            
    low+=lim
    high+=lim
        