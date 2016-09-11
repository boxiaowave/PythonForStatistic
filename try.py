# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 11:41:59 2016

@author: BoXiao
"""
import time
import random
import string
#file = open('words.txt')
#
#count1 = 0
#count2 = 0
#for line in file:
#    count1+=1.0
#    if not 'e' in line.strip():
#        print line.strip()
#        count2+=1
#        
#print count2/count1

#def is_reverse(nu):
#    if nu[:]==nu[::-1]:
#        return True
#    return False
#    
#def is_fit(nu):
#    if is_reverse(str(nu)[-4:]):
#        if is_reverse(str(nu+1)[-5:]):
#            if is_reverse(str(nu+2)[-5:-1]):
#                if is_reverse(str(nu+3)[:]):
#                    return True
#    return False
#    
#for i in range(100000,1000000):
#    if is_fit(i):
#        print i
#        
#def count_time(b):
#    count=0
#    now_age=0
#    a=0
#    while a<100 and b<100:
#        if str(a).zfill(2)==str(b).zfill(2)[::-1]:
#            count+=1
#            if count == 6:
#                now_age=a,b
#        a+=1
#        b+=1
#    return [count,now_age]
#    
#for i in range(99):
#    if count_time(i)[0]==8:
#        print count_time(i)[1]
#        
#def readtxtap(f):
#    t=time.time()    
#    s=[]
#    for i in f:
#        s.append(i.strip())
#    print len(s)
#    return time.time()-t
#    
#   
#def readtxtplus(f):
#    t=time.time()    
#    s=[]
#    for i in f:
#        s = s + [i.strip()]
#    print len(s)
#    return time.time()-t         
#            

'''
def getf(f):
    s = dict()
    for i in f:
        i=i.strip()
        sort_i=tuple(sorted(i))
        if not sort_i in s:
            s[sort_i]=[i]
        else:
            s[sort_i].append(i)
    return s


with open('words.txt') as file:
    tup=getf(file)
    longest = []
    for key,value in tup.iteritems():
        if len(value)>1:
            longest.append((len(value),value))
    longest.sort(reverse=True)
    for tim,value in longest[:]:
        print value 
'''

def histogram(s):
    d=dict()
    for i in s:
        d[i]=d.get(i,0)+1
    return d

def chose_from_hist(s):
    t=[]
    for key,value in s.items():
        t.extend([key]*value)
    return random.choice(t)
    
anu=0
bnu=0

hist = histogram('aabb')
for i in range(400):
    if chose_from_hist(hist)=='a':
        anu+=1
    else:
        bnu+=1

def process_file(f,delete=True):
    hist=dict()
    if delete:
        for line in f:
            if line.startswith('*END*THE SMALL PRINT!'):
                break
    for line in f:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line =  line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.whitespace+string.punctuation)
        word=word.lower()
        hist[word]=hist.get(word,0)+1

def print_most_common(hist,n=10):
    s=[]
    for key,value in hist.items():
        s.append((value,key))
    s.sort(reverse=True)
    for key,value in s[:n]:
        print value,'\t',key

def substract1(d1,d2):
    s=dict()
    for key in d1:
        if not key in d2:
            s[key]=None
    return s

def substract2(d1,d2):
    return set(d1.keys()).difference(set(d2.keys()))
    
with open('emma.txt') as file:  
    hist1 = process_file(file)

with open('words.txt') as file:  
    hist2 = process_file(file,False)
    
print sum(hist1.values()) 
print len(hist1.keys())    
print_most_common(hist1,12)

histdiff=substract1(hist1,hist2)
for words in histdiff:
    print words,

s1=set(histdiff.keys())
print '\n -----this is line------\n'
    
histdiff=substract2(hist1,hist2)
for words in histdiff:
    print words,   
    
print '\n'
print histdiff.difference(s1)