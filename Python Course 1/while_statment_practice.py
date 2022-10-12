#building set of numbers
s = None
l = None
while True:
    num = input("Enter a number: ")
    #done checker
    if num == "done":
        break
    #word v number checker
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    #finding smallest
    if s == None:
        s = fnum
    elif s > fnum:
        s = fnum
    #finding largest
    if l is None:
        l = fnum
    elif l < fnum:
        l = fnum
l = int(l)
s = int(s)
print('Maximum is', l)
print('Minimum is', s)
