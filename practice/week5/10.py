#HelloMyDear
#_hello_my_dear
import re

def replacer(match):
   return match.group('a')+"_"+match.group('x').lower()+match.group('b')


def checker(text, pattern):
   result=re.sub(pattern, replacer, text)
   print (result)


text=input()
pattern=r'(?P<a>[a-z]*)(?P<x>[A-Z])(?P<b>[a-z]*)'
checker(text, pattern)