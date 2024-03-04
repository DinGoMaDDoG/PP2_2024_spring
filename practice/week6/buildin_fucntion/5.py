x=(1, "HI", True, "Hwle")
result=True

for i in x:
  if i==False:
    result=False
    break

if result:
  print("True")
else: 
  print("False")