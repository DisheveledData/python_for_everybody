#imports
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re
sumofnumbers = 0

#url managment
url = input('URL PLEASE -')
print('Getting URL:', url)
file = urllib.request.urlopen(url)
decoded = file.read().decode()
print('Length in Characters:', len(decoded))

#json managment
injs = json.loads(decoded)

for item in injs['comments']:
    newnum = item['count']
    newnum = int(newnum)
    sumofnumbers = sumofnumbers + newnum
print(sumofnumbers)
