import os

path=input("Enter a path to a file: ")

with open (path, 'a') as file:
  file.write(input("Ender the list:"))