# by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com
# this code is made for Python 2.7.s vor Python 3.x.x use input() instead of raw_input()
# small url link web extractor program

import urllib
import re

url = raw_input('Enter URL >> ')
html = urllib.urlopen(url).read()

urllinks = re.findall('href="(http://.*?)"', html) 

for link in urllinks:
    print link