def solve (numheads, numlegs):
  initialnumheads=numheads
  numheads=numheads*2
  numlegs=(numlegs-numheads)/2
  print (f"The number of rabbits: {numlegs}, The number of chicken: {initialnumheads-numlegs}")

print("Enter the number of heads, legs: ")
solve(int(input()), int(input()))


  