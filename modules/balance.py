import locale
import os
from modules.account import Account, balance


class Balance(Account):
    prompt = 'Account Balance'

    @classmethod
    def transact(cls):
        locale.setlocale(locale.LC_ALL, '')
        current_bal = locale.currency(balance[0], grouping=True)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n   Your balance is: {}".format(current_bal))
