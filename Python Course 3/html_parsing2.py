#imports
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignoring SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#loop that goes 3 hyperlinks in, makes that the new link and repeats 3 times
y = input('ENTER URL - ')
loopcount = 0
BigLoopNumber = input('How Many Pages Deep')
SmallLoopNumber = input('How Many Links Deep')
try:
    BigLoopNumber = float(BigLoopNumber)
except:
    print('Enter a Nummber Please')
    BigLoopNumber = input('How Many Pages Deep')
    BigLoopNumber = float(BigLoopNumber)
try:
    SmallLoopNumber = float(SmallLoopNumber)
except:
    print('Enter a Nummber Please')
    SmallLoopNumber = input('How Many Links Deep')
    SmallLoopNumber = float(SmallLoopNumber)
while loopcount <= (BigLoopNumber - 1):
    url = y
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    num = 0
    for tag in tags:
        if num >= (SmallLoopNumber):
            break
        else:
            y = (tag.get('href', None))
            num = num + 1
    loopcount = loopcount + 1

#printing the name
linkstring = str(y)
name = re.findall('http://py4e-data.dr-chuck.net/known_by_(.*?)\.html', linkstring)
print(name)
