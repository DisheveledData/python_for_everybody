#opening file
file = input('FILE: ')
if len(file) < 1:
    file = "mbox-short.txt"
fileo = open(file)
#selecting lines with from
filelist = list()
for line in fileo:
    if line.startswith('From:'):
        splitupline = line.split()
        filelist.append(splitupline[1])
    else:
        continue
#taking names and constructing histogram
dictofnames = dict()
for name in filelist:
    dictofnames[name] = dictofnames.get(name, 0) + 1
#pulling largest paired data
largestemail = None
largestcount = None
for name,count in dictofnames.items():
    if largestcount is None or count > largestcount:
        largestcount = count
        largestemail = name
#output
print(largestemail, largestcount)
