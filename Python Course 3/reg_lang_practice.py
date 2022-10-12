import re
#open on input
file = input('FILE: ')
fileo = open(file)
#list creation and number insert
listofnums=list()
for line in fileo:
    line = line.rstrip()
    templist = re.findall("[0-9]+", line)
    listofnums = listofnums + templist
#floating all items in listofnums
listofints = list()
for items in listofnums:
    nownumeric = int(items)
    listofints.append(nownumeric)

#summing listofnums
sumofints = sum(listofints)
#output
print(sumofints)
