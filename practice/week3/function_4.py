def counter (x):
  result=0
  for i in range (1, x+1 ):
    if (x % i ==0):
      result+=1
  return result

def isPrime(i):
   if counter(i)==2:
    print(i)
   elif i==1:
    print(i)

n=input() 
mylist=n.split()
for i in mylist:
  isPrime(int(i))
