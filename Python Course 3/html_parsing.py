#imports
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignoring SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url input and debug
url = input('ENTER URL - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#parsing out the number from  anchor tags
sum=0
tags = soup('span')
for tag in tags:
    x=str(tag)
    y= re.findall("[0-9]+",x)
    for number in y:
        number=float(number)
        sum = sum + number

#output
sum = int(sum)
print(sum)
