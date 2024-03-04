import os

path=input()

#print(os.listdir(path))

obj=os.scandir(path)

for i in obj:
  print (i.name)