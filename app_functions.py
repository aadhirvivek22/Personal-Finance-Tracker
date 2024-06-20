from accounts import Accounts
from transactions import Transaction
from utilities import *
from tabulate import tabulate
import random
import string
import os
import json


def add_transaction(account):
    """
    Prompts the user to add a transaction (either deposit or expense) to the account.

    Args:
        account (Accounts): An instance of the Accounts class representing the user's account.

    Returns:
        None
    """
    while True:
        while True:
            transaction_type = input("Was the transaction a deposit or expense? (deposit/expense): ").strip().lower()
            if transaction_type in ['deposit', 'expense']:
                break
            else:
                print("Invalid transaction request! Please input deposit or expense only.")
    
        amount = get_numeric_input()
        transaction_id = generate_id(account.transactions)
        current_transaction = Transaction(transaction_id, amount, transaction_type)
        account.transactions.append(current_transaction.create_transaction(amount, transaction_type))
        if transaction_type == 'deposit':
            account.account_balance += amount
        else:
            account.account_balance -= amount
        status_list=[['Transaction ID', 'Transaction Amount', 'Transaction Type'], [transaction_id, amount, transaction_type]]    
        print("Transaction added!")
        print(tabulate(status_list, tablefmt='outline', headers='firstrow'))
        leave = input("Press enter to finalize transactions, or any other key to add more transactions: ")
        if leave == '':
            print("Process complete.")
            break
        else:
            print("Continuing transaction process...")

    print(f"Your account balance after these transactions is {account.account_balance}")

def undo_transaction(account):
    """
    Prompts the user to remove a transaction by ID and restores the account balance.

    Args:
        account (Accounts): An instance of the Accounts class representing the user's account.

    Returns:
        None
    """
    while True:
        remove_transaction = input("Enter transaction ID to remove: ").upper()
        status_list = [['Transaction ID', 'Transaction Amount', 'Transaction Type']]
        for i in range(1, len(account.transactions)):
            if remove_transaction == next(iter(account.transactions[i].keys())):
                amount = account.transactions[i][remove_transaction][0]
                type = account.transactions[i][remove_transaction][1]
                status_list.append([remove_transaction, amount, type])
                print(tabulate(status_list, tablefmt='outline', headers='firstrow'))
                confirm = get_yes_no()
                if confirm:
                    account.transactions.pop(i)
                    restore_balance(account, amount, type)
                    print("Transaction has been removed.")
                else:
                    print("Removal cancelled.")
                break
        else:
            print("Transaction ID not found.")
        
        leave = input("Press enter to exit removal process, or any other key to continue: ")
        if leave == '':
            print("Process complete.")
            break
        else:
            print("Continuing removal process...")

def view_transactions(account):
    """
    Displays the transaction history of the account in a tabular format.

    Args:
        account (Accounts): An instance of the Accounts class representing the user's account.

    Returns:
        None
    """
    header = list(account.transactions[0])  # Get header from first transaction entry
    transactions = [header]

    for transaction in account.transactions[1:]:
        key = next(iter(transaction))
        transactions.append([key, transaction[key][0], transaction[key][1]])

    print(tabulate(transactions, tablefmt='grid', headers='firstrow'))

def display_balance(account):
    """
    Displays the current balance of the account.

    Args:
        account (Accounts): An instance of the Accounts class representing the user's account.

    Returns:
        None
    """
    print("Your account balance is:", account.account_balance)