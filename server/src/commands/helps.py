from commands.base_command import Command
class Help(Command):
    def exec(self):
        help_line = "Hello there and welcome to bridge\nThe following commands will allow you to use our service to it's fullest capibilities\n!weather;City -- Allows you to get the weather in your city of choice\n!stock;stockname or\n!stock;stock1;stock2... -- Allows you to check any stocks you'd like courtesy of Yahoo Finance\n!mail;recipient;subject;mail_body or\n!mail;recipient1,recipient2;subject;mail_body -- Allows you to send emails\n!translate;word;targetlanguage -- Allows you to translate"
        return help_line