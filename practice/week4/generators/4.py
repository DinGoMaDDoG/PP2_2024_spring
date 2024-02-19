def squares (a, b):
  while a<b+1:
    yield a**2
    a+=1


a=int(input("Enter a:"))
b=int(input("Enter b:"))

for i in squares(a, b):
  print(i)