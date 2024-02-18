'''def my_gen(n):
  i=1
  while i<n:
    yield i**2
    i+=1


n=int(input())
for i in my_gen(n):
  print(i)'''

n=int(input())
my_gen= (i**2 for i in range (n))

for i in my_gen:
  print (i)