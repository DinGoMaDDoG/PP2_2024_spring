from itertools import permutations

print ("Enter word:")
x=input()
a=permutations(x)
for i in a:
  print (i)