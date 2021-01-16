# Import Libraries
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from twilio.rest import Client
from commands import commands
import config
import requests

# Flask app configuration
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize Twilio client configuration
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)


# Validate Message
def execute_command(message):
    # read the first command token and strip the "!"
    command = message.split(' ')[0][1:]

    
    if command not in commands:
        client.messages.create(
            messaging_service_sid='MG0974823613bcb3dd8987e1dc8b58eda7',
            body='Type "!help" to get more info!',
            to='+17809530388'
        )
        # send "type !help to get more information"
        return

    # otherwise, we know the command exists
    cmd = commands[command](message)
    cmd.exec()


# Send Message
@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def send_message():
    if request.method == 'POST':
        message = client.messages.create(
            messaging_service_sid='MG0974823613bcb3dd8987e1dc8b58eda7',
            body='Testing',
            to='+14168980216'
        )
        return "<h1>Success</h1>"
    else:
        return ""


# Main Driver
if __name__ == "__main__":
    app.run(host='0.0.0.0')

