#!pip install deal 

import unittest
import deal

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


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_transfer_to(self):
        recipient_account = BankAccount(500)
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)
        self.assertEqual(recipient_account.get_balance(), 500)

    def test_transfer_from(self):
        sender_account = BankAccount(500)
        sender_account.deposit(250)
        self.assertEqual(sender_account.get_balance(), 750)
        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
