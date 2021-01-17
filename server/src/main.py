# Import Libraries
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from commands import commands
import config
import requests
import commands.utils
from commands import *

# Flask app configuration
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize Twilio client configuration
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

# Send Message
@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def send_message():
    if request.method == 'POST':
        message = client.messages.create(
            from_= config.Twilio_number,
            body='Testing',
            to = config.reciever
        )
        return "<h1>Success</h1>"
    else:
        return ""

# Reply to SMS


@app.route("/reply", methods=['GET', 'POST'])
@cross_origin()
def reply():
    body = request.values.get('Body', None)
    command = base_command.Command(body).command
    if command == "stock":
        response = stock.Stock(body)
        return_text = response.exec()
    elif command == "mail":
        response = mail.Mail(body)
        return_text = response.exec()

    res = MessagingResponse()
    if return_text == '':
        res.message("please type !help for response")
    else:
        res.message(return_text)
    return str(res)


# Main Driver
if __name__ == "__main__":
    app.run(host='0.0.0.0')
