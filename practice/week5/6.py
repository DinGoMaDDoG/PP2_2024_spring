import re


txt=input() 
pattern=r"[\s,.]"
x=re.sub(pattern, ":", txt)
print(x)