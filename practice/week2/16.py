mylist=[ "Run", "Right", "Reason"]

for x in mylist:
  print (x)

print("\n")
  
for i in range(len(mylist)):
  print (mylist[i])

print("\n")

i=0

while i<len(mylist):
  print(mylist[i])
  i+=1

print("\n")

[print(x) for x in mylist] 