def counter (x):
  result=0
  for i in range (1, x):
    if (x % i ==0):
      result+=result
  return result

def isPrime(i):
   if counter(i)==2:
    print(i)

n=input() 
mylist=n.split()
for i in mylist:
  isPrime(int(i))
