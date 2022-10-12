# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
numberofnumbs = 0
total = 0
for line in fh:
    #dets based on start of line
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #singles out all of the numbers and floats them
    spaceplace = line.find(' ')
    float(spaceplace)
    line = line[spaceplace:]
    line = line.strip()
    line = float(line)
    #totals the lines determined above
    total = total + line
    total = float(total)
    #counts up how many floated numbers we have
    numberofnumbs = numberofnumbs + 1
    numberofnumbs = float(numberofnumbs)
#avg operations
avgofspamnumbers = (total) / (numberofnumbs)
print("Average spam confidence:", avgofspamnumbers)
