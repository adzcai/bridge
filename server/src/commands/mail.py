import smtplib, ssl
from commands.base_command import Command
from commands.utils import send_mail

class Mail(Command):
    def exec(self):
        """Command for emailing a user.

        Format:
        !mail;email1@email.com, email2@email.com;subject;body
        """ 
        emails = self.args[0].split(',')
        for email in emails:
            send_mail(self.args[1], self.args[2], email)
        return_text = "Sent Mail To :: " + self.args[0] +"\n" + self.args[1] + ":\n" + self.args[2]
        return return_text
