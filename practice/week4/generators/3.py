def my_gen(n):
  i=1
  while i<n:
    if i % 3==0 and i % 4 ==0:
      yield i
    i+=1

n=int(input("Num:"))

for i in my_gen(n):
  print(i)