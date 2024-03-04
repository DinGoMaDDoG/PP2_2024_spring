import os

path=input("Enter file to delete: ")

if os.path.exists(path): 
  if os.access(path, os.X_OK):
    os.remove(path)
else:
  print("file does not exist")