from commands.base_command import Command
from commands.utils import find_movie


class Movie(Command):
    help_msg="!movie;[title;][rating;][score;][casting;][directors;][synopsis]"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def exec(self):
        print("ARGS", self.args)

        if len(self.args) == 0:
            return "Type !help to get information about Bridge."

        title, year, rating, score, casting, directors, synopsis = find_movie(self.args[0])

        return_message=''

        for arg in self.args[1:]:
            arg = arg.lower()
            if arg == 'title':
                return_message += title + "\n"
            elif arg == 'year':
                return_message += year + "\n"
            elif arg == 'rating':
                return_message += rating + "\n"
            elif arg == 'score':
                return_message += score + "\n"
            elif arg == 'casting':
                return_message += casting + "\n"
            elif arg == 'director':
                return_message += directors + "\n"
            elif arg == 'synopsis':
                return_message += synopsis + "\n"

        print("RETURN MESSAGE:", return_message)

        return str(return_message)
