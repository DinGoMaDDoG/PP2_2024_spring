import math

class Point:
  def __init__(self):
    self.fcoor=int(input())
    self.scoor=int(input())
  def show (self):
    print (f"the first coordinate is {self.fcoor}")
    print (f"the second coordinate is {self.scoor}")
  def move(self):
    print("Do you want to change coordinates? (YES || NO):")
    self.ans=input()
    if self.ans=="YES":
       return self.__init__(), self.show(), self.move()
    else:
      return 0
  def dist(self, x1, y1, x2, y2):
      print(f"The distance between two points is {math.sqrt((x2-x1)**2 +(y2-y1)**2 )}")
    
x=Point()
x.show()
x.move()
print ("Enter the coordinates of two points (x1, y1, x2, y2):")
x.dist(int(input()), int(input()), int(input()),int(input()))