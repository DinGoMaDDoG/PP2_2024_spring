def Unique_elements(cat):
  cat2=[]
  for i in cat:
    if i not in cat2:
      cat2.append(i)

       
  print (cat2)

print("Enter list:")
a=input()
cat=a.split()

Unique_elements(cat)


# r 3 r 5 r 6 r 7 