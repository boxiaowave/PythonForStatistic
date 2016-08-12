# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:14:42 2016

@author: BoXiao
"""

def InsertSort(li):
    for i in range(1,len(li)):
        if li[i]>li[i-1]:
            temp = li[i]
            print li[i]
            for j in range(i):
                if temp<li[i-j-1]:
                    li[i-j]=li[i-j-1]
                    li[i-j-1] = temp
                else:
                    break
    return li
    
li = [12,11,13,9,7,4,2,1]
    
print InsertSort(li)