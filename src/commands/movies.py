from commands.base_command import Command
from commands.utils import find_movie


class Movie(Command):
    help_msg="!movie;[title;][rating;][score;][cast;][directors;][synopsis]"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def exec(self):
        print("ARGS", self.args)

        if len(self.args) == 0:
            return "Type !help to get information about Bridge."

        data = find_movie(self.args[0])

        print(data)

        return_message=''

        for arg in self.args[1:]:
            arg = arg.lower()
            if arg == 'title':
                return_message += "Title: " + data["Title"] + "\n"
            elif arg == 'year':
                return_message += "Year: " + str(data["Year"]) + "\n"
            elif arg == 'rating':
                return_message += "IMDB rating: " + str(data["IMDB"]) + "\n"
            elif arg == 'score':
                return_message += "Tomatometer score: " + str(data["Tomatometer"]) + "\n"
            elif arg == 'cast':
                return_message += "Cast: " + ', '.join(data["Cast"]) + "\n"
            elif arg == 'director':
                return_message += "Director(s): " + data["Directors"] + "\n"
            elif arg == 'synopsis':
                return_message += "Synopsis: " + data["Plot"] + "\n"

        print("RETURN MESSAGE:", return_message)

        return return_message
