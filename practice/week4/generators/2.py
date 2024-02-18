n=int(input())
my_gen=(i for i in range (1, n) if i%2==0)

for i in my_gen:
  print(f"{i:,}")