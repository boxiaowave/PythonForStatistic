# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:49:38 2016

@author: BoXiao
"""

def selectionsort(li):
    #保证原始列表不被修改    
    li = li[:]
    sortli=[]
    for j in range(len(li)):
        index = 0
        for i in range(len(li)):
            if li[i]<li[index]:
                index = i
        sortli.append(li.pop(index))
    return sortli

if __name__=='__main__':
    
    li = [12,11,10,9,7,4,2,1]
    
    print selectionsort(li)
    print li
        