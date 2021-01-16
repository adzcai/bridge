from typing import no_type_check_decorator
from commands.mail import Mail
from commands.tweet import Tweet
from commands.stock import Stock

commands = {
  "mail": Mail,
  "tweet": Tweet,
  "stock": Stock
}
