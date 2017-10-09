import re
file1 = open('sample.rtf')
sumhere = []
x = file1.read()
here = re.findall('[0-9]+',x)
sumlist = 0
if len(here) > 0:
    for x in here:
        sumlist += int(x)
print(len(here))
print(sumlist)
