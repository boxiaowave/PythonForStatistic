# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:48:52 2016

@author: BoXiao
"""

def bubblesort(li):
    flag = 0
    for j in range(0,len(li)-1):
        if flag == 1:
            return li
        flag = 1
        for i in range(0,len(li)-1-j):
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
                flag = 0
    return li

print bubblesort([11,10,8,7,6,5,4,3,2,1])
