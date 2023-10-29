'''implement a class a bankAccount that represents a bank account.
The class should have private attributes for account number,
account holder name, and account balance. include methods to deposit money, withdraw money,and display
account balance.
ensure that the account balance cannot be accessed directly from outside the class'''


class bankaccount:
 
def__init__(self,account_number, account_holder_name,initial_balance=0.0):
self.__account_number=account_number
self.__account_holder_name=account_holder_name
self.__account_balance=initial_balance

def deposit(self, amount):
 if amount>0:
   self._account_balance +=amount
   #self.__account_balance=self.__account_balance+amount
   print("deposited ₹ {}.new balance:₹{}". format (amount,self.__account_balance))
  
 else:
   print("individual deposit amount.")

def withdraw (self, amount):
  if amount>0 and amount<=self.__account_balance:
    self.__account_balance-=amount
    print("withdrew ₹{} .new balance:₹{} ".format(amount,self.__account_balance))
    
  else:
    print("invalid withdrawal amount or insufficient balance.")

def display _balance(self):
  print("account balance for {} (account #{} ):₹{} ".format(self.__account_holder_name,self.__account_number,self.__account_balance))



#create an instance of the bank account class
account=bankaccount (account _number="123456789", account_holder_name="hari prabu",initial_balance=5,000.0)

#test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()


  

