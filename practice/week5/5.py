import re

txt=input()
pattern=r"a.*b$"
x=re.search(pattern, txt)
print(x)