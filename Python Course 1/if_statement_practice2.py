hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
r = float(rt)
def computepay(h, r):
    if h < 40:
        pay = (h * r)
        return (pay)
    else:
        pay = (40 * r) + ((h-40) * r * 1.5)
        return (pay)
p = computepay(h, r)
print('Pay', p)
