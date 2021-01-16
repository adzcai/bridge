from typing import no_type_check_decorator
import commands.mail
import commands.tweet
import commands.stock

commands = {
  "mail": commands.mail.Mail,
  "tweet": commands.tweet.Tweet,
  # "stock": commands.stock.Stock
}
