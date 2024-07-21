# 24. Write a Python class to implement a basic bank account 
# with methods to deposit and withdraw money.

class Bank:
    def __init__(self, balance):
        self.balance = balance

    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Deposited {amount}. New balance: {self.balance}")

account = Bank(1000)
dep = 250
wd = 1000

print(f"Current balance: ${account.check_balance()}")
account.deposit(dep)
account.withdraw(wd)
