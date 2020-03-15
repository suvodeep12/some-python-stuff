import re
#numbers = []
total = 0
fname = input("Enter file:")
if len(fname) < 1 : fname="regex_sum_42.txt"
handle = open(fname)
for line in handle:
    numbers = re.findall("[0-9]+",line)
    if not numbers: continue
    else:         
        for num in numbers:
            total = total + int(num)
print(total)