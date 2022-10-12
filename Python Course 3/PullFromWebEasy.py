#HTML
import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen('url')
for line in file:
    print(line.decode().strip())

#Strings and make histogram
counts = dict()
for line in name:
    words = line.decode().split()
    for word in words:
        counts[word]=counts.get(word, 0)+ 1
print(counts)
