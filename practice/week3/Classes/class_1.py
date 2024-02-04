class String_work:
  def __init__(self, mystring):
    self.mystring=mystring
  def printString(self):
    print (self.mystring.upper())

p1=String_work(input())
p1.printString()
