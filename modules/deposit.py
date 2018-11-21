from modules.account import Account, balance


class Deposit(Account):
    prompt = 'Deposit money'

    def action(self, amount):
        balance[0] = balance[0] + amount
        print(f'{amount} deposited successfully')

    @classmethod
    def transact(cls):
        amount = float(input('How much do you want to deposit? '))
        cls.action(cls, amount)
