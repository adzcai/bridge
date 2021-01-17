class Command:
    """Base class for defining new commands.

    Each subclass should define an exec function which runs the command.

    The command format is as follows:
    !command <args>
    body
    """

    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.parse()

    def exec(self, command):
        raise Exception('All subclasses must implement the exec method!')

    # static command to parse a command string
    def parse(self):
        """Parses the raw text into a header and a command body.
        
        `header` is a string containing the first line of the text and
        `self.body` is a list containing the remaining lines of the text.
        `header` is further split into the command and the remaining args
        """
        header, *self.body = self.raw_text.splitlines()
        self.command, *self.args = map(str.strip, header.split(';'))
        if self.command.startswith('!'):
            self.command = self.command[1:] # remove the initial "!"
