from accounts import Accounts
from transactions import Transaction
from app_functions import *
from utilities import *
from tabulate import tabulate
import random
import string
import os
import json

def main_menu(account):

    """
    Displays the main menu of the Personal Finance Tracker application and processes user input.

    Args:
        account (Accounts): An instance of the Accounts class representing the user's account.

    Returns:
        None
    """
    speak(f'Welcome to Personal Finance Tracker, {account.username}')
    print("\nWelcome to Personal Finance Tracker")
    while True:
        print("1. Add Transaction")
        print("2. View Transaction History")
        print("3. Display Balance")
        print("4. Undo Transaction")
        print("5. Exit")
        speak("Enter your choice: ")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(account)
        elif choice == '2':
            view_transactions(account)
        elif choice == '3':
            display_balance(account)
        elif choice == '4':
            undo_transaction(account)
        elif choice == '5':
            speak('Thank you, see you again!')
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    accounts = load_accounts()
    username = input("Enter username: ")
    account = get_account(username, accounts)

    main_menu(account)
    save_accounts(accounts)