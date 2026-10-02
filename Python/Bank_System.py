from random import randint
Account_holder={}
class Bank_System:

  def __init__(self):
    print("Welcome to Our Bank !")

  def create_account(self,name,account_no,pin_no):
    self.name=name
    self.account_no=account_no
    self.pin_no=pin_no
    self.amount=0
    Account_holder[account_no]={'name':name,'pin_no':pin_no,'amount':self.amount}
    print("Account successfully created!")
  def deposit(self,account_no):
    if(account_no in Account_holder):
      print(f"hello, {Account_holder[account_no]['name']}")
      pin=int(input("Enter Pin No:"))
      if(pin==Account_holder[account_no]['pin_no']):
        print("Pin match!")
        amt=float(input("Enter Amount for Deposit:"))
        Account_holder[account_no]['amount']+=amt
        print("Amount deposited successfully!")
      else:
        print("Incorrect Pin!")
    else:
      print("Not a Account Holder")
  def withdraw(self,account_no):
    if(account_no in Account_holder):
      print(f"hello, {Account_holder[account_no]['name']}")
      pin=int(input("Enter Pin No:"))
      if(pin==Account_holder[account_no]['pin_no']):
        print("Pin match!")
        amt=float(input("Enter Amount for Withdraw:"))
        if(amt<=Account_holder[account_no]['amount']):
          Account_holder[account_no]['amount']-=amt
          print("Amount Withdrawed successfully!")
        else:
          print("Insufficient Amount!")
      else:
        print("Incorrect Pin!")
    else:
      print("Not a Account Holder")

  def display_info(self,account_no):
    if(account_no in Account_holder):
      print(f"hello, {Account_holder[account_no]['name']}")
      pin=int(input("Enter Pin No:"))
      if(pin==Account_holder[account_no]['pin_no']):
        print("Pin match!")
        print("======Detail======")
        print("Name: ",Account_holder[account_no]['name'] )
        print("Balance: ",Account_holder[account_no]['amount'] )
        print("==============================================")
        print()
      else:
        print("Incorrect Pin!")
    else:
      print("Not a Account Holder")

bk=Bank_System()
while True:
  print("Menu")
  print("1. Create Account")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Balance Enquiry")
  print("5. Exit")

  ch=int(input("Enter your choice:"))
  if ch==1:
    name=input("Enter your name:")
    account_no=randint(11111111111111,99999999999999)
    print("Account number:",account_no)
    pin_no=int(input("Enter 4 digit pin no:"))
    bk.create_account(name,account_no,pin_no)
    print("=======================================")
  elif ch==2:
    account_no=int(input("Enter your account_no"))
    bk.deposit(account_no)
    print("=======================================")
  elif ch==3:
    account_no=int(input("Enter your account_no"))
    bk.withdraw(account_no)
    print("=======================================")
  elif ch==4:
    account_no=int(input("Enter your account_no"))
    bk.display_info(account_no)
    print("=======================================")
  elif ch==5:
    break
  else:
    print("Invalid choice")









