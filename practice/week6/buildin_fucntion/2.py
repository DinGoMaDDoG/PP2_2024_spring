str=input()

Lcount=Ucount=0

for i in str:
  if (i.isupper()):
    Ucount+=1
  elif i.islower():
    Lcount+=1

print (f"The num of lower case latters is {Lcount}")
print (f"The num of upper case latters is {Ucount}")