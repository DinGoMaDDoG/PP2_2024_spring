a=input()
b=[]

for i in a.split():
   b.append(int(i))

result=1

for i in b:
   result=result*i

print (result)