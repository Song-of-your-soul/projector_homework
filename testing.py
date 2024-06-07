import unittest
import builtins
from unittest.mock import Mock, patch

class Account:
    def __init__(self, balance: int, account_number: int):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account number: {self._account_number}, balance: {self._balance}"


class SavingsAccount(Account):
    def __init__(self, balance: int, account_number: int):
        super().__init__(balance, account_number)
        self.interest = balance / 5

    def gain_interest(self):
        self._balance += self.interest


class CurrentAccount(Account):
    def __init__(self, balance: int, account_number: int, overdraft_limit: int):
        super().__init__(balance, account_number)
        self.limit = overdraft_limit
    
    def send_overdraft_letter(self):
        if self.limit > self._balance:
            print(f"Overdraft letter sent for Account {self._account_number}")


class Bank:
    def __init__(self, accounts: dict):
        self.accounts = accounts

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.gain_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def open_account(self, account_number: int):
        self.accounts.update({account_number: Account.create_account(account_number)})

    def close_account(self, account_number: int):
        if account_number in accounts.keys():
            self.accounts.pop(account_number)

    def dividends(self, money: int):
        for account in accounts.keys():
            accounts[account]._balance += money

good_account = SavingsAccount(2000, 101)
bad_account = CurrentAccount(500, 102, 1000)
okay_account = SavingsAccount(1000, 103)
just_okay_account = CurrentAccount(1000, 104, 900)

accounts = {
    good_account._account_number: good_account,
    bad_account._account_number: bad_account,
    okay_account._account_number: okay_account,
    just_okay_account._account_number: just_okay_account
}


blank_account = {}
new_bank = Bank(blank_account)
old_bank = Bank(accounts)


class TestBank(unittest.TestCase):
    def test_Bank(self):
        with self.assertRaises(TypeError):
            no_bank = Bank()

    def test_open_account(self):
        new_bank.open_account(101)
        for account in new_bank.accounts.values():
            self.assertIsInstance(account, Account)
            self.assertEqual(account._balance, 0.0)
        
    def test_update(self):
        with patch('builtins.print') as mocked_print:
            old_bank.update_accounts()
            self.assertEqual(good_account._balance, 2400)
            mocked_print.assert_called_once()


unittest.main()