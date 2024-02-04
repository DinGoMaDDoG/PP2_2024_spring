def reverser(string):
  for i in range (len(string)-1, -1, -1):
    print (string[i])
  #string.reverse()
  #print (string)

print ("Enter sentence:")
a=input()
string=a.split()
reverser(string)