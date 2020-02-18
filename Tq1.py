# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 01:37:10 2019

@author: Talib
"""

def specialnumbers():
    a = list(map(int,input("Enter the list of numbers\n").split()))
    
    totalsum = []
    for i in a:
        facsum = 0
        if(i==1):
            facsum = 0
        else:
            for j in range(1,(i//2)+1):
                if(i%j==0):
                    #print(j)
                    facsum+=j
        totalsum.append(facsum)
        #print(totalsum)
        
    result = []
    for i in totalsum:
        if(i in a):
            result.append(a[totalsum.index(i)])
            
    if(len(result)>0):    
        return  result
    else:
        return "No special numbers present"

        
        