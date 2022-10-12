# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for vari in fh:
    vari = vari.rstrip()
    vari = vari.upper()
    print(vari)
