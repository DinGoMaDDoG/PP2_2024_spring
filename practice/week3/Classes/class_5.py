class Account:
  def __init__(self, owner, balance):
    self.owner=owner
    self.balance=balance
    self.num=0
    self.initialdeposit=self.balance
    self.withdrawmoney=0
    self.withdrawans="NO"
    self.balance_for_withdraw=-1



  def Mybank (self):
    if (self.balance_for_withdraw<self.balance and self.balance_for_withdraw>=0):
      print (f"\nYour current balance is: {self.balance_for_withdraw}")
    elif (self.balance>=self.balance_for_withdraw):
      print (f"\nYour current balance is: {self.balance}")
    
    if self.num<=1:
     print (f"You have {self.num} deposit")
     print (f"Total amount of money in deposit: {self.initialdeposit-self.balance}")
    else:
     print (f"You have {self.num} deposits")
     print (f"Total amount of money in deposit: {self.initialdeposit-self.balance}")
    if self.withdrawans=="YES":
      print (f"You have withdrawn {self.balance-self.balance_for_withdraw}")



  def deposit(self):
    print ("Create deposit? (YES || NO):")
    self.ans=input()
    if self.ans=="YES":
      print("How much would you like to put in deposit?:")
      self.mydeposit=float(input())
      if self.balance-self.mydeposit<0:
        print ("\nInvalid command! Not enough money to put into deposit")
        return self.Mybank(),self.deposit()
      else:
        self.balance=self.balance-self.mydeposit
        self.num+=1
        return self.Mybank(), self.deposit()
    else:
        return self.Mybank()
    


  def withdraw(self):
    self.balance_for_withdraw=self.balance
    print("Would you like to withdraw money from balance? (YES || NO):")
    self.withdrawans=input()
    if self.withdrawans=="YES":
      print ("How much would you like to withdraw:")
      self.withdrawmoney=float(input())
      if self.balance_for_withdraw-self.withdrawmoney<0:
        print ("\nInvalid command! Not enough money in balance")
        return self.Mybank(),self.withdraw()
      else:
        self.balance_for_withdraw=self.balance_for_withdraw-self.withdrawmoney
        return self.Mybank()
    else:
      return self.Mybank()
  


print ("Enter your name:")
owner=input()
print ("Enter your balance:")
balance=float(input())


account=Account(owner, balance)
account.Mybank()
account.deposit()
account.withdraw()
