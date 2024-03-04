import os


i=65
while(i<=90):
  filename=f"container\\{chr(i)}.txt"
  file=open(filename, 'w')
  file.close()
  i+=1



