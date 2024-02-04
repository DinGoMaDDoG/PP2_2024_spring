import random

class Family:
  def __init__(self, name):
    self.count=0
    self.name=name
    self.initial_num=random.randint(1, 20)

  def Guesser(self):
   print ("Take a guess.")
   self.num=int(input())
   if (self.initial_num==self.num):
     print (f"Good job, {self.name}! You guessed my number in {self.count+1} guesses!")
   elif (self.initial_num>self.num):
     print("Your guess is too low.")
     self.count+=1
     return self.Guesser()
   else:
     print("Your guess is too high.")
     self.count+=1
     return self.Guesser()
  



print ("Hello, What is your name?")
name=input()
print (f"Well,{name}, I am thinking of a number between 1 and 20.")
x=Family(name)
x.Guesser()