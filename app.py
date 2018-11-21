import os
import locale
import sys
from modules.account import Account

all_actions = [cls for cls in Account.__subclasses__()]


class Teller():
    """This class is the interface to a customer's bank account"""

    def build_menu(self):
        """Construct the main menu items for the command line user interface"""

        # Clear the console first
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Enter a number to perform a transaction: ')

        for action in all_actions:
            print(f'{all_actions.index(action) + 1}. {action().prompt}')

    def start_service(self):
        self.build_menu()
        choice = int(input(">> "))

        if choice > len(all_actions) or choice < 1:
            self.start_service()
        action = all_actions[choice - 1]
        action.transact()
        another = input('Perform another transaction? (Y/any): ')

        if another.lower() == 'y':
            self.start_service()
        sys.exit('Thank you for banking with us')


if __name__ == "__main__":
    Teller().start_service()
