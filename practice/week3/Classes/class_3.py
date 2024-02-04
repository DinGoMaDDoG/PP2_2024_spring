class Shape:
  def __init__(self):
    pass
  def Area(self):
    return 0
  
class Rectangle(Shape):
  def __init__(self):
    print("Enter length:")
    self.length=float(input())
    print("Enter width:")
    self.width=float(input())
  def area(self):
    print (f"the area of rectangle is {self.length*self.width}")

x=Rectangle()
x.area()