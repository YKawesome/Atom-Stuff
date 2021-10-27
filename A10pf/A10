import re

fhandle = open("ADA10.txt")
listnum = list()
for line in fhandle:
     templist = re.findall('[0-9]+',line)
     listnum = listnum + templist

sum = 0

for number in listnum:
    sum = sum + int(number)

print(sum)
