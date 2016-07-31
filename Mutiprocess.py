#!/usr/bin/env python
#--*-- coding=utf-8 --*--

import os
import re
from multiprocessing import Pool
import time
import random
import threading
# import pdb
print 'Prosscess(%s) starts...' % os.getpid()
'''
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.'% (os.getpid(),os.getppid())
else:
    print 'I (%s) just created a child process(%s).' % (os.getpid(),pid)
'''
# k=re.compile(r'(hello)')
#
# st=re.search(k,'hello,hghellosds!!')
#
# print st.group(1).title()

# from multiprocessing import Process
#
# def runc(name):
#     print 'this is ',name,'-',os.getpid()
#
# if __name__=='__main__':
#     print 'Parent process is ',os.getpid()
#     p=Process(target=runc,args=('test',))
#     print 'process starts'
#     p.start()
#     p.join()
#     print 'end child process'
#     print os.getpid()


# def long_time(name):
#     print 'run task is',name,'-',os.getpid()
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print 'run task (',name,'),for ',end-start
#
# if __name__=='__main__':
#     print 'Parent process is ',os.getpid()
#     p=Pool()
#     for i in range(5):
#         p.apply_async(long_time,args=(i,))
#     print 'wait all subprocesses'
#     p.close()
#     p.join()
#     print 'done'

def loop(s):
    print 'thread '+threading.current_thread().name+' starts running'
    print s
    for n in range(5):
        print 'thread'+threading.current_thread().name,'>>',n
        time.sleep(1)
    print 'thread '+threading.current_thread().name+' ends'

if __name__=='__main__':
    print 'thread ' + threading.current_thread().name + ' starts running'
    t=threading.Thread(target=loop,name='child',args=('test',))
    t.start()
    t.join()
    print 'thread ' + threading.current_thread().name + ' ends'




