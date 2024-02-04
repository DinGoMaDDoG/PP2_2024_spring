def spy_game(nums):
  x1=x2=x3=-1
  for i in range(0, len(nums)):
    if nums[i]==0:
       x2=i
    if nums[i]==7:
        x3=i
  for i in range(0, len(nums)):
   if nums[i]==0 :
        x1=i
        break
  '''if x1+x2+x3=="007":
     print("True")
  else:
     print ("False")'''
  if x1<x2<x3:
     print ("True")
  else:
     print("False")
        
#nums=([1,2,4,0,0,7,5]) #--> True
#nums=([1,0,2,4,0,5,7]) #--> True
#nums=([1,7,2,0,4,5,0]) #--> False
    

nums=[]
a=input()
for x in a.split():
   nums.append(int(x))

spy_game(nums)