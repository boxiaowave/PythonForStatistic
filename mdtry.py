# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:07:37 2016

@author: BoXiao
"""
'''
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
'''

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
        
# from visual import *
#
# scene.range=(256,256,256)
# scene.center=(128,128,128)
#
# color = (0.1,0.1,0.9)
#
# # sphere(pos=scene.center,radius=128,color=color)
# t = range(0,256,51)
#
# for x in t:
#     for y in t:
#         for z in t:
#             pos = x,y,z
#             color = x/255.0,y/255.0,z/255.0
#             sphere(pos=pos,radius=10,color=color)

'''
class Card(object):
    suitnames = ['Clue','Diamond','Hearts','Spades']
    ranknames = [None,'Ace','1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s,%s' %(Card.suitnames[self.suit],Card.ranknames[self.rank])

    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)

po =Card(1,2)
po2 = Card(2,1)

print cmp(po,po2)

class deck(object):

'''
from swampy.Gui import *
g = Gui()
g.title('GUI')



def make_button():
     g.bu(text='button1', command=make_label)

def make_label():
     g.la(text='Well Done!!')

def make_circle():
    global item
    item=canvas.circle([0, 0], 100, fill='red')

def change_color():
    try:
        item.config(fill=entry.get())
        text.delete(0.0,END)
        text.insert(END,'right input')
    except:
        text.delete(0.0,END)
        text.insert(END,'wrong color, please change input and press button again')



canvas = g.ca(width=500,height=500)
canvas.config(bg='green')
# canvas.rectangle([[-50,-50],[50,50]],fill='blue',outline='orange',width=100)
# canvas.oval([[0,0],[200,100]],fill='yellow',outline='red',width=5)
button = g.bu(text="let's try", command=make_circle)
# canvas.line([[0,0],[30,30],[100,50],[0,0]],fill='green',width=3)
# canvas.polygon([[-10,-10],[100,100],[120,80]],fill='red',width=3)
#item = canvas.circle([0,0],100,fill='red')
#item.config(fill='blue',outline='orange',width=10)
entry = g.en(text='input color name')
text = g.te(width=100,height=5)
button2 = g.bu(text='change the color of circle',command=change_color)
g.mainloop()
