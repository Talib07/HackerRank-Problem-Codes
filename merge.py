# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 01:07:56 2019

@author: Talib
"""

def countInversions(arr):
    counter = 0
    b = len(arr)
    for j in range(b):
        print("Outer loop no" + str(j))
        for i in range(1,len(arr)):
            print("Inner loop no" + str(i))
            if(arr[i-1]>arr[i]):
                arr[i-1],arr[i] = arr[i],arr[i-1]
                counter+=1
             #   print(arr)
            #print(arr)
        arr = arr[0:len(arr)-1]
        print(len(arr))
        
    return counter