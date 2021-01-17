import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from commands.base_command import Command
from commands.utils import check_price

class Stock(Command):
    def exec(self):
        return_text = ""
        for stock in self.args[0].split(','):
            title, price, currency = check_price(stock.strip())
            return_text += title + ", " + price+  ", " + currency + '\n'
        return return_text