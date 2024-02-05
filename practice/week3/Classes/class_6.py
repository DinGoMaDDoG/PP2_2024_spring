def isPrime(a):
  if a<2:
    return False
  for i in range (2, a):
     if a%i==0:
       return False
  return True

def myfilter (mylist):
  return (a for a in mylist if isPrime(a))


a=input()
mylist=[]
for i in a.split():
  mylist.append(int(i))
  
my_new_list=myfilter(mylist)
print (my_new_list)