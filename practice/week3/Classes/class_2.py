class Shape:
  def __init__(self):
    pass
  def Area(self):
    return 0


class Square(Shape):
  def __init__(self):
    self.length=float(input())
  def Area(self):
    print (self.length*self.length)


x=Square()
x.Area()