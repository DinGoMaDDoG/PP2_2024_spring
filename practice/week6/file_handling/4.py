import os

path=input()

if os.path.exists(path):
  with open (path) as file:
    print(len(file.readlines()))
else:
  print("File does not exist")
