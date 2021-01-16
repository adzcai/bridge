import smtplib, ssl
from commands.base_command import Command

class Mail(Command):
    """Command for emailing a user.

    Format:
    !mail;email1@email.com, email2@email.com;subject;body
    """

    def __init__(self, raw_text):
      super().__init__(raw_text)

    def exec(self, parsed):
        to, subject = map(str.split, self.header)

        print(to, subject)
