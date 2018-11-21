from modules.account import Account, balance


class Withdraw(Account):
    prompt = 'Withdraw money'

    def acton(self, amount):
        if balance[0] - amount < 0:
            print('Insufficient balance, try a lower amount')
        else:
            balance[0] = balance[0] - amount
            print(f'{amount} withdrawn successfully')

    @classmethod
    def transact(cls):
        amount = float(input('How much do you wish to withdraw? '))
        cls.acton(cls, amount)
