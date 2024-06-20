import unittest
from accounts import Accounts, Transaction
from main_menu import *

class TestAccounts(unittest.TestCase):

    def setUp(self):
        self.account = Accounts("test_user", 1000)
        self.transaction = Transaction('GHTYZ', 1000, 'deposit')

        self.assertEqual((self.account).username, 'test_user')
        self.assertEqual((self.account).account_balance, 1000)

    def test_create_transaction(self):
        
        self.assertEqual(self.transaction.create_transaction(100, 'deposit'), {'GHTYZ': [1000, 'deposit']})

    def test_generate_id(self):
        existing_ids = ['ABCDE', '12345']
        new_id = generate_id(existing_ids)
        self.assertNotIn(new_id, existing_ids)
        
    def test_validate_numeric_input(self):
        with self.assertRaises(ValueError):
            validate_numeric_input("eleven")

        with self.assertRaises(ValueError):
            validate_numeric_input("one")

        assert(validate_numeric_input("1000") == 1000)
    
    def test_validate_yes_no_input(self):

        assert(validate_yes_no_input('Y') == True)
        assert(validate_yes_no_input('y') == True)
        assert(validate_yes_no_input('N') == False)
        assert(validate_yes_no_input('n') == False)

        with self.assertRaises(ValueError):
            validate_yes_no_input("YES")

        with self.assertRaises(ValueError):
            validate_yes_no_input("no")
    
    def test_restore_balance(self):
        account = Accounts('test', 600)
        restore_balance(account, 400.0, 'deposit')
        assert(account.account_balance, 1000)

        with self.assertRaises(ValueError):
            restore_balance('lol',400.0, 'deposit')
        
        with self.assertRaises(ValueError):
            restore_balance(account ,'r', 'deposit')
        
        with self.assertRaises(ValueError):
            restore_balance(account ,400.0, 1)

if __name__ == '__main__':
    unittest.main()