
n=int(input("Enter n:"))
my_gen=(i for i in range (n, -1, -1))

for i in my_gen:
  print (i)