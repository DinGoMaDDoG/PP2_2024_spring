a=input()

b=""

for i in range (len(a)-1, -1,-1):
  b+=a[i]

if a ==b:
  print("polindrom")

else:
  print ("not polindrom") 