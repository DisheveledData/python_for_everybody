#(1/5)opening the file
file = input('File Name:')
fileo = open(file)
fileo = fileo.read()
#(2/5)using split on space
files = fileo.split()
#(3/5) append list
fileso = []
for item in files:
    if item not in fileso:
        fileso.append(item)
#(4/5) sort on alpha
fileso.sort()
#(5/5) printing
print(fileso)
