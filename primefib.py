# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:28:20 2019

@author: Talib
"""
import math
#from itertools import combinations
prime1 = []
def getprime(a,b):
    for i in range(a,b+1):
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                break
        else:
            prime1.append(i)
    return prime1

def primecheck(a):
    if(a==2):
        return 1
    else:
        flag=1
        for i in range(2,int(math.sqrt(a))+1):
            if(a%i==0):
                flag=0
                break
        if(flag==1):
            return(1)
        else:
            return 0
            
def primecomb(a):
    m=[]
    for i in range(len(a)):
        str1 = ""
        str1 += str(a[i])
        for j in range(len(a)):
            if(j==i):
                continue
            str1 += str(a[j])
            k = int(str1)
            if primecheck(k)==1:    
                m.append(k)
            str1 = str(a[i])
    mi=min(m)
    ma=max(m)
    l=len(set(m))
    s1=mi
    s2=ma
    for i in range(2,l):
        s3=s1+s2
        s1=s2
        s2=s3
    return s3           
 

l=input().split()
print(primecomb(getprime(int(l[0]),int(l[1]))))
         