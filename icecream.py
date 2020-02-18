# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:45:05 2019

@author: Talib
"""

def whatFlavors(cost, money):
    arr = cost[:]
    cost.sort()
    
    i = cost.index(cost[0])
    j = cost.index(cost[-1])
    
    while(cost[i]+cost[j]!=money):
        if(cost[i]+cost[j]>money):
            j-=1
            #print("True")
        elif(cost[i]+cost[j]<money):
            #print("False")
            i+=1
            
    a=min(arr.index(cost[i])+1,arr.index(cost[j])+1)
    b=max(arr.index(cost[i])+1,arr.index(cost[j])+1)
    #print(cost[i],cost[j])
    
    if(cost[i]==cost[j]):
        #print("True")
        #print(a)
        k = arr[a::]
        #print("sliced array")
        #print(k)
        #print(cost[j])
        #print(k.index(cost[j]))
        b = a + (k.index(cost[j]))+1 
        
    print(a,b)
    #print(min(i+1,j+1),arr[min(i+1,j+1)-1],max(i+1,j+1),arr[max(i+1,j+1)-1])
    
    '''for i in cost:
        temp = i
        ind1 = cost.index(temp)
        #print(temp)
        cost[ind1] = 0
        #print(cost)
        if(money-temp in cost):
            #print("True")
            #a=max(money-temp,temp)
            a = money - temp
            ind2 = cost.index(a)
            cost[ind2] = 0
            #b=min(money-temp,temp)
            #res2 = cost.index(b)
            #cost[cost.index(b)] = 0
            #print(i,money-i,a,b)
            break
        else:
            #print("False")
            continue
    print(min(ind1+1,ind2+1),max(ind1+1,ind2+1))