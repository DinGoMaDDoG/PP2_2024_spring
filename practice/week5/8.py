import re
text=input()
x=re.findall("[a-z]*[A-Z][a-z]*", text)
print(x)