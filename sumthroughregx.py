name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
totalno=list()
sumt=0
#count=0
import re
for line in handle:
    line=line.strip()
    if re.search('[0-9]+',line):
        no=re.findall('[0-9]+',line)
        for n in no:
            sumt=sumt+float(n)
            #count=count+1
            
print(sumt)
#print(count)
