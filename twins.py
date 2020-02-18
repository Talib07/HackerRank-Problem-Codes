# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:28:29 2019

@author: Talib
"""

def separate(a):

    val = True
    res = []
    temp = []
    eg = ['1','2','3','4','5','6','7','8','9','0']
        
    for i in a:    
        if(i in eg):        
            print("Number")
            if(val == True):
                print("Number before strings")
                temp.append(i)
            else:
                print("number after string")
                if(len(res)!=0):
                    print("First number")
                    res.append(int("".join(map(str,temp))))
                    temp = []
                    temp.append(i)
                else:
                    temp.append(i)
                    val = True
                
        else:
            print("string")
            val = False
    return temp
    return res    