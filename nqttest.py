# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:42:38 2019

@author: Talib
"""

x= input()
lst1 = [int(i) for i in str(x)]
num = sum(lst1)
lst2 = [int(i) for i in str(num)]
lst2.reverse()
s = [str(i) for i in lst2]
res = int("".join(s))
if(res*num == x):
    print("{} is magic number".format(x))
else:
    print("{} is not a magic number".format(x))
