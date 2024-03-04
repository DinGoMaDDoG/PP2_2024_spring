import os

read=False
write=False
execute=False
exist=False

def Checker(path):
 try:
   if(os.path.exists(path)):
     exist=True
     print ("The file exist")
     if(os.access(path, os.R_OK)):
       read=True
       print("The file is readable")
     if os.access(path, os.W_OK):
       write=True
       print ("The file is writeable")
     if os.access(path, os.X_OK):
       execute=True
       print("The file is executeable")
   else:
    print ("The file does not exist")
 except FileNotFoundError:
  print("The file was not found")

path=input()

Checker(path)


