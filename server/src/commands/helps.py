from commands.base_command import Command


class Help(Command):
    def exec(self):
        help_line = """Hello there! Welcome to Bridge!
The following commands will allow you to use our service to its fullest capibilities:
!weather;city -- Allows you to get the weather in your city of choice.
!stock;stockname or
!stock;stock1;stock2... -- Allows you to check any stocks you'd like, courtesy of Yahoo Finance.
!mail;recipient;subject;mail_body or
!mail;recipient1,recipient2;subject;mail_body -- Allows you to send emails
!translate;word;target_language -- Allows you to translate from one language to another"""
        return help_line
