import re


snake=input()
x=re.sub("_([a-z]+)",lambda x: x.group(1).capitalize(), snake)
print(x)

