text = "X-DSPAM-Confidence:    0.8475"
spcount = text.find(' ')
spcount = int(spcount)
nobeg = text[spcount:]
float(nobeg)
print(nobeg.lstrip())
