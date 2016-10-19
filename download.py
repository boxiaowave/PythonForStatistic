import urllib2
import urllib
from bs4 import BeautifulSoup

html='http://www.tingvoa.com/html/20130204/1404.html'

ddir='./machinelearning/'
f=urllib2.urlopen(html)
s=BeautifulSoup(f,'lxml')

t=s.find('div',id='download')

urls=t.find_all('a')
for url in urls[10:]:
    urllib.urlretrieve(url['href'],ddir+url.text.encode('utf8')+'.mp4')
    print url.text+'download is done'
