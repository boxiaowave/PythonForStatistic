# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 11:46:29 2016

@author: BoXiao
"""

import csv

file = open('./test.csv', 'wb+')

writer = csv.writer(file)
writer.writerow(('number', 'number*2', 'number**2'))
for i in range(50):
    writer.writerow((i, i*2, i**2))

file.close()
