#opening file
file = input('FILE: ')
if len(file) < 1:
    file = "mbox-short.txt"
fileo = open(file)
#pull out the time
listoftimes = list()
for lines in fileo:
    if lines.startswith('From '):
        colonbased = lines.split(':')
        inclutime = colonbased[0]
        hourtimelist = inclutime.split()
        listoftimes.append(hourtimelist[5])
#mkae the historgam
dictofhours = dict()
for hours in listoftimes:
    dictofhours[hours] = dictofhours.get(hours, 0) + 1
#print
for k,v in sorted(dictofhours.items()):
    print(k,v)
