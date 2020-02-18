# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 00:39:37 2019

@author: Talib
"""

def rotLeft(a, d):
    for i in range(d):
        a.append(a[0])
        a.remove(a[0])
    return a
    