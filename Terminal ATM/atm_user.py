
from datetime import datetime


class user:
    def __init__(self, User, Password):
        self.UserID = User  # 4 Digit Number Stored As String
        self.UserPin = Password  # 4 Digit Number Stored As String
        # Every Transaction Will Be Stored As A String And Will Be Displayed As A List
        self.UserTransactionHistory = []
        self.AccountBalance = 0  # Account Balance Stored As A Int

    def check_balance(self):
        print(f"Your balance is ${self.AccountBalance}")

    def deposit(self, amount):
        today = datetime.now()
        self.AccountBalance += amount
        self.UserTransactionHistory.append(f"{today} : Deposited ${amount}")
        print(
            f"You Deposited {amount}. Your new balance is ${self.AccountBalance}")

    def withdraw(self, amount):
        today = datetime.now()
        self.AccountBalance -= amount
        self.UserTransactionHistory.append(f"{today} : Withdrew ${amount}")
        print(
            f"You Withdew {amount}. Your new balance is ${self.AccountBalance}")

    def view_transaction_history(self):
        for transactions in self.UserTransactionHistory:
            print(transactions)
