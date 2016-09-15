# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:07:37 2016

@author: BoXiao
"""

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return '%d,%d' %(self.x,self.y)
    
    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        else:
            return Point(self.x+other[0],self.y+other[1])
            
class Kangaroo(object):
    def __init__(self,contents=None):
        if contents == None:
            contents=[]
        self.pouch_contents=contents
        
    def put_in_touch(self,a):
        self.pouch_contents.append(a)
        
    def __str__(self):
        return '%s' %self.pouch_contents
        
kangra = Kangaroo()
roo = Kangaroo()

kangra.put_in_touch('yusdhs')
kangra.put_in_touch(roo)

print kangra
print roo

"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""
'''
class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print kanga
print roo
'''
# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.
        
from visual import *

scene.range=(256,256,256)  
scene.center=(128,128,128)

color = (0.1,0.1,0.9)

sphere(pos=scene.center,radius=128,color=color)     




          
