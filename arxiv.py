#-*- coding: utf-8 -*-
# ******************************************************
# Author       : BoXiao
# Last modified: 2016-07-23 02:48
# Email        : xbustc@gmail.com
# Filename     : arxiv.py
# Description  :
# ******************************************************
import urllib
from bs4 import BeautifulSoup
import re
import os


homep = 'http://arxiv.org'


f = urllib.urlopen('http://arxiv.org/list/cond-mat.quant-gas/recent')

'''
file = open('page.txt','w')
file.write(f.read())
file.close()
file = open('page.txt','r')
a = BeautifulSoup(file.read(),'lxml')
'''

a = BeautifulSoup(f, 'lxml')


tili = []
tili2 = []
authorli = []
tidic = dict()

s = a.find_all(['dd', 'h3'])
authorsname = ''
i = 0
abdo = a.find_all('a', title='Abstract')

for dot in s:
    if dot.name == 'dd':
        for tag in dot.find_all('div', class_='list-title mathjax'):
            title = ' '.join(
                (tag.span.string+tag.span.next_sibling.string).encode('utf-8').split())
        for tag in dot.find_all('div', class_='list-authors'):
            Authors = 'Authors: ' + \
                ','.join([authors.string for authors in tag.find_all('a')])
        tili.append(title)
        tili2.append(title)
        authorli.append(Authors)
        tidic[title] = [i+1, time, Authors]
        i += 1
    else:
        time = dot.string.encode('utf - 8')
        tili.append('Date:' + time)


def input_nu():
    while True:
        try:
            while True:
                numbers = int(
                    raw_input('\nwhich paper?[Input the number,input 0 to abort]'))
                if 0 <= numbers < len(tidic):
                    return numbers
                    break
                else:
                    print 'out of range,please input again.'
            break
        except:
            print 'Please input the right number\n'


def show_paperlist():
    for value in tili:
        if value.startswith('Date'):
            print '\n', value, '\n'
        else:
            print '\n', tidic[value][0], '.', value
            print tidic[value][2]


def show_paperlistlat():
    print '\n', tili[0]
    for value in tili2:
        if tidic[value][1] in tili[0]:
            print '\n', tidic[value][0], '.', value
            print tidic[value][2]


def show_authors(i):
    print '\n', tili2[i - 1], '\n', authorli[i-1]


def show_abstract(i):
    abst = urllib.urlopen(homep + abdo[i - 1]['href'])
    absoup = BeautifulSoup(abst, 'lxml')
    print '\n', tili2[i - 1], '\nAbstract:', absoup.blockquote.contents[2].lstrip()


def download_file(i):
    abst = urllib.urlopen(homep + abdo[i - 1]['href'])
    absoup = BeautifulSoup(abst, 'lxml')
    download_url = absoup.find('a', accesskey='f')['href']
    print 'downloading~~~biu~~biu~~biu~~'
    paperdir = './arxivpapers/' + tidic[tili2[i - 1]][1][:16]
    if not os.path.exists(paperdir):
        os.makedirs(paperdir)
    urllib.urlretrieve(homep + download_url, paperdir +
                       '/' + ' '.join(tili2[i - 1].split()[1:7]) + '.pdf')
    print 'done.:-D'


# print tili
def next_step():
    print '\nWhat do you want me to do next?'
    print u'[0]给朕退下。'
    print '[1]Show the abstract.'
    print '[2]Show the author of the paper.'
    print '[3]Download the pdf file.'
    print '[4]Show the paper list again.'
    print '[5]Show the paper list in the latest day.'
    term = int(raw_input('Please choose:'))
    if term == 0:
        print u'\n欢迎下次使用.'
    elif term == 4:
        show_paperlist()
        next_step()
    elif term == 5:
        show_paperlistlat()
        next_step()
    elif term in range(0, 4):
        papernumber = input_nu()
        if papernumber == 0:
            next_step()
        elif term == 1:
            show_abstract(papernumber)
            next_step()
        elif term == 2:
            show_authors(papernumber)
            next_step()
        elif term == 3:
            download_file(papernumber)
            next_step()
        elif term == 0:
            print "Abort"
            next_step()
    else:
        print 'Wrong Input'
        next_step()


show_paperlist()
print '\n~~~Welcome to ArXiv paper scraping program~~~~'
next_step()
