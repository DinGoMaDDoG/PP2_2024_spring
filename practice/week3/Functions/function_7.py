def has_33(nums):
  b=False
  for i in range (0, len(nums)-1):
    if nums[i]==nums[i+1]==3:
      b=True
      break
  if(b==True):
    print("True")
  else:
    print("False")
      
#nums=list((1, 2, 3 , 4, 5, 6))
nums=list((1, 1, 2 , 2, 3, 3))
has_33(nums)
