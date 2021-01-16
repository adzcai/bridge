import sys
sys.path.append("../src/commands")
from mail import Mail

cmd = Mail('''!mail; alexandercai@outlook.com; "Hello world"
To Whom it May Concern:
I hope you have a good day!
Sincerely,
Me''')

print('raw text:', cmd.raw_text)
print("command:", cmd.command)
print("args:", cmd.args)
print("body:", cmd.body)

# cmd.exec()
