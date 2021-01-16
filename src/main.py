# Import Libraries
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from twilio.rest import Client
import config
import requests
import parse

from commands import Command

# Flask app configuration
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize Twilio client configuration
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

# Send Message


def receive_message(message):
    cmd = Command(message)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def send_message():
    if request.method == 'POST':
        message = client.messages.create(
            from_='+18189462554',
            body='ok hands',
            to='+16472364001'
        )
        return "<h1>Success</h1>"
    else:
        return ""


# Main Driver
if __name__ == "__main__":
    app.run(host='0.0.0.0')

