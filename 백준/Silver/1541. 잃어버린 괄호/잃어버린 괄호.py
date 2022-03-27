import re

cal = input()

cal_sep = cal.split('-')
cc = [re.sub(r'\b0+(?!\b)','',i) for i in cal_sep]

total = eval(cc[0])

for i in range(1,len(cc)):
    total -= eval(cc[i])

print(total)