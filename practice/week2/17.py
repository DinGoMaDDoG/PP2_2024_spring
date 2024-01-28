mylist=["hi", "Hello", "Good"]


newlist=[]
for x in mylist:
  if "hi" in x:
    newlist.append(x)

print (newlist)


newnewlist=[x for x in mylist if "hi" in x]
print (newnewlist)


supernewlist=[x for x in mylist if x!="Bye"]
print (supernewlist)

biglist=[x for x in range (11)]
print (biglist)


biglist2=[x for x in range (11) if x%2==0]
print (biglist2)


biglist3=[x.upper() for x in mylist]
print (biglist3)


biglist4=[x if x!="Hello" else "Bye" for x in mylist]
print (biglist4)