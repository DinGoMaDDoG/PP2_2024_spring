import re

def Matcher(txt):
  pattern=r"ab{2,3}"
  x=re.search(pattern, txt)
  print(x)


txt=input()
Matcher(txt)