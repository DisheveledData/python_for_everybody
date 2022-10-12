import xml.etree.ElementTree as ET
import re
import socket
import urllib.request, urllib.parse, urllib.error
sumdigits = 0
numberofnumbers = 0
#specifying data
url = input('URL PLEASE -')
print('Getting URL:', url)
file = urllib.request.urlopen(url).read()
print('Length in Characters:', len(file))


#tree and parsing
tree = ET.fromstring(file)
lst = tree.findall('comments/comment')
for number in lst:
    digit = number.find('count').text
    digit = float(digit)
    sumdigits = sumdigits + digit
    numberofnumbers = numberofnumbers + 1
sum = int(sumdigits)
print('Count:', numberofnumbers)
print('Sum:', sum)
