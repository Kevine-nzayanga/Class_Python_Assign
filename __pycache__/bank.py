# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
class Bank:
    bank="World Bank"
    def __init__(self,name,saving,balance):
        self.name=name
        self.saving=saving
        self.balance=balance
    def withdrawal(self,amount):
        total=self.balance-amount
        return total
    def details(self):
        return (f"The owner of this account is {self.name}")    
    
    def check_balance(self):
        return (f" Hello {self.name}, this is your balance:{self.balance} {self.withdrawal(32)}")
    
Bank_of_Africa= Bank("Marcus",1234,23000)
print(Bank_of_Africa.details())
print(Bank_of_Africa.withdrawal(2000))
print(Bank_of_Africa.check_balance())


