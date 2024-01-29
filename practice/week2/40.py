mychildren={
  "1child":{
    "name": "James",
    "year": "2001",
  },
  "2child":{
    "name": "Huana",
    "year": "2002",
  },
  "3child":{
    "name": "Diego",
    "year": "2003",
  }
}

print (mychildren)
print (mychildren["2child"]["year"])
print (mychildren["2child"])

for x in mychildren:
  print(mychildren[x])