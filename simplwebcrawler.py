# by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com
# Simple web crawler searching for url links and following them
# This code is for Python 2.7.x for Python 3.x.x need to replace raw_input() with input()

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL >> ')
count = int(raw_input('Enter Count - '))
position = int(raw_input('Enter Position - '))

for _ in xrange(0,count): # _ is used as a throw-away name; xrange() is used due large number of counts
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

    url = tags[position-1].get('href')

print (url)