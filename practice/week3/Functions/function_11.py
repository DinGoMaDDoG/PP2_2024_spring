def Pal (cat):
  cat2=""
  for i in range (len(cat)-1, -1, -1 ):
    cat2+=cat[i]
  if (cat==cat2):
    print ("True")
  else:
    print ("False")

print ("Enter word:")
cat=input()
Pal (cat)