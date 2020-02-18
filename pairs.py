# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:25:40 2019

@author: Talib
"""

def pairs(k, arr):
    arr.sort()
    count = 0
    l = r = 0 

    while(r<len(arr)):
        if(arr[r]-arr[l]==k):
            count+=1
            #print("true1")
            print(arr[l],arr[r])
            l+=1
            r+=1
        elif(arr[r]-arr[l]<k):
            #print("true2")
            r+=1
            #print(l,r)
        elif(arr[r]-arr[l]>k):
            #print("true3")
            l+=1
                    
    return count