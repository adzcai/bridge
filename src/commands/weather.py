from commands.base_command import Command
from commands.utils import check_weather
class Weather(Command):
    def exec(self):
        """
        !weather;City
        """
        return check_weather(self.args[0])