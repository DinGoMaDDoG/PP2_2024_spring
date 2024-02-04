import math


def Volume(R):
  return (4/3*math.pi*R**3)

print ("Enter Radius:")
R=float(input())
print (Volume(R))