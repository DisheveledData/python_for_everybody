hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
r = float(rt)
if h < 40 :
    pay = (h * r)
    print(pay)
else :
    pay = (40 * r) + ((h-40) * r * 1.5)
    print(pay)
