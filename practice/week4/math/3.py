import math

print("Input number of sides:")
n=int(input())
print("Input the length of a side:")
a=float(input())
P=a*n
apothem=a/(2*math.tan(math.radians(180/n)))
S=P*apothem/2
print(f"The area of the polygon is:{round(S)}")
