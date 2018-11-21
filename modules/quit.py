import sys
from modules.account import Account


class Quit(Account):
    prompt = 'Quit'

    @classmethod
    def transact(cls):
        sys.exit('Thank you for banking with us')
