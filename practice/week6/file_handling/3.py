import os

path=input()

if os.path.exists(path):
  print(os.path.split(path))