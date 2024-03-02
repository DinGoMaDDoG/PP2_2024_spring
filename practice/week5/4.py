import re

def f(txt):
  pattern=r"[A-Z][a-z]{2,}"
  x=re.search(pattern, txt)
  print(x)


txt=input()
f(txt)