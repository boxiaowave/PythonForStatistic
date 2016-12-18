# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:54:23 2016

@author: BoXiao
"""
import SelectionSort

def mergesort(l1, l2):
    li = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            li.append(l1[i])
            i += 1
        else:
            li.append(l2[j])
            j += 1
    li += l1[i:]
    li += l2[j:]
    return li

l1 = SelectionSort.selectionsort([2, 8, 3, 2, 6])
l2 = SelectionSort.selectionsort([1, 9, 3, 1, 34, 0])

print mergesort(l1, l2)
