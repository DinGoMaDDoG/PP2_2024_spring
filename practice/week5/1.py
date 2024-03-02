import re

txt=input()
pattern=r"ab*"
x=re.search(pattern, txt)
print(x)