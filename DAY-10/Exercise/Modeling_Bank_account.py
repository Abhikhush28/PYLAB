class BankAccount:
 def __init__(self, account_number, name, balance=0):
  self.account_number = account_number
  self.name = name
  self.balance = balance
 
 def deposit(self, amount):
  self.balance += amount
 
 def withdraw(self, amount):
  if self.balance >= amount:
   self.balance -= amount
  else:
   print("Insufficient funds")

 def check_balance(self):
  print(f"Balance: {self.balance}")



acct1 = BankAccount("12345", "John Doe", 500)
acct2 = BankAccount("2345", "jane doe")

acct1.deposit(100)
acct1.check_balance()

acct1.withdraw(100)
acct1.check_balance()