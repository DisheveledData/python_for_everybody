# open and error
file = input("FILE: ")
if len(file) < 1:
    file = "mbox-short.txt"
fileo = open(file)
#list creation
fl=list()
for line in fileo:
    if line.startswith("From:"):
        splitup=line.split()
        fl.append(splitup[1])
    else:
        continue
#printing
for item in fl:
    print(item)
print("There were", len(fl), "lines in the file with From as the first word")
