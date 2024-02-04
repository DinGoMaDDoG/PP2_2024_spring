def Unique_elements(cat):
  cat2=[]
  for i in range (0, len(cat)+1):
    for j in range (i+1, len(cat)+1):
      if cat[i]==cat[j]:
        cat2.append(cat[i])
        cat.remove(cat[j])
       
  print (cat2)

print("Enter list:")
cat=list(input())
Unique_elements(cat)


# r 3 r 5 r 6 r 7 