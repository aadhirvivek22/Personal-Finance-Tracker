import csv
import json

class Accounts:

    def __init__(self, username, account_balance) -> None:
        self.username = username
        self.transactions = [['Transaction ID', 'Transaction Amount', 'Transaction Type']]
        self.account_balance = account_balance

    def view_balance(self):
        return self.account_balance

    def to_dict(self):
        return {
            "username": self.username,
            "transactions": self.transactions,
            "account_balance": self.account_balance
        }

    @classmethod
    def from_dict(cls, data):
        account = cls(data['username'], data['account_balance'])
        account.transactions = data['transactions']
        return account

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return cls.from_dict(data)



