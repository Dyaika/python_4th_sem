#!pip install deal

import deal

@deal.inv(lambda self: self.balance >= 0)
class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        
    def deposit(self, amount: float):
        self.balance += amount
        
    @deal.pre(lambda self, amount: amount <= self.balance)
    def withdraw(self, amount: float):
        self.balance -= amount
        
    def get_balance(self):
        return self.balance

#ba = BankAccount(-10)
ba = BankAccount(10)
#ba.withdraw(100)
