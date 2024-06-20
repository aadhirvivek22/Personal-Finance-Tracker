# Helper functions for file handling
from accounts import *
from transactions import *
import random
import os
import string
import json

def load_accounts(filename='accounts_data.json'):
    """
    Load all accounts from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: A dictionary of username to Accounts objects.
    """
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                accounts = {user_data['username']: Accounts.from_dict(user_data) for user_data in data}
                return accounts
        except json.JSONDecodeError as e:
            print(f"Error loading accounts from {filename}: {e}")
            return {}
    else:
        print(f"No accounts file found. Starting with an empty list.")
        return {}

def save_accounts(accounts, filename='accounts_data.json'):
    """
    Save all accounts to a JSON file.

    Args:
        accounts (dict): A dictionary of username to Accounts objects.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    data = [account.to_dict() for account in accounts.values()]
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
            print(f"Accounts successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")

    # Verify if the file was created successfully
    if os.path.exists(filename):
        print(f"Verified that {filename} was created.")
    else:
        print(f"Error: {filename} was not created.")

def get_account(username, accounts):
    """
    Retrieve an account by username, creating a new one if it doesn't exist.

    Args:
        username (str): The username to search for.
        accounts (dict): A dictionary of username to Accounts objects.

    Returns:
        Accounts: The Accounts object for the given username.
    """
    if username in accounts:
        print(f"Welcome back {username}!")
        return accounts[username]
    else:
        print(f"No account found for username '{username}'. Creating a new account.")
        account_balance = float(input("Enter account balance: "))
        account = Accounts(username, account_balance)
        accounts[username] = account
        return account

# Helper function for user input checks

def get_numeric_input():
    """
    Prompts the user to enter a numeric input until a valid number is provided.

    Args:
        None

    Returns:
        float: The numeric input provided by the user.
    """
    while True:
        user_input = (input("Enter the amount: "))
        try:
            return validate_numeric_input(user_input)
        except ValueError:
            print("Invalid input! Expected a number.")

def validate_numeric_input(value):
    try:
        check_val = float(value)
        return check_val
    except:
        raise ValueError("Please enter a number!")

def get_yes_no():
    """
    Prompts the user to enter 'yes' or 'no' and keeps prompting until valid input is received.

    Args:
        None

    Returns:
        bool: True if the user inputs 'yes', False if the user inputs 'no'.
    """
    while True:
        user_input = (input('Are you sure you want to remove this transaction? (Y/N)').strip())
        
        if type(validate_yes_no_input(user_input))==bool:
            return validate_yes_no_input(user_input)
        else:
            pass

def validate_yes_no_input(user_input):
    try:
        user_input=user_input.upper()
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter 'Y' or 'N'.")
        


# Helper functions to generate IDs and restore account balance

def generate_id(transactions: list):
    """
    Generates a unique 5-character ID for a transaction.

    Args:
        transactions (list): List of existing transactions.

    Returns:
        str: A unique 5-character transaction ID.
    """
    success = False
    while not success:
        id = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(5)])
        if not any(id in transaction for transaction in transactions):
            success = True
    return id

def restore_balance(account: Accounts, amount: float, transaction_type: str):
    """
    Restores the account balance based on the type of transaction.

    Args:
        account (Accounts): The account to restore balance for.
        amount (float): The transaction amount.
        type (str): The type of transaction ('deposit' or 'expense').

    Returns:
        None
    """
    if type(account)!=Accounts or type(amount)!=float or type(transaction_type)!=str:
        raise ValueError
    if transaction_type == 'deposit':
        account.account_balance -= amount
    else:
        account.account_balance += amount