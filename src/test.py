# Import Libraries
from flask import Flask
from flask_cors import CORS, cross_origin
from twilio.rest import Client
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

# Send Message
@app.route("/")
@cross_origin()
def send_message():
    # message = client.messages.create(
    #     from_='+18189462554',
    #     body='ok hands',
    #     to='+14168980216'
    # )
    return "<h1>jazz hands</h1>"


# Main Driver
if __name__ == "__main__":
    app.run(host="0.0.0.0")
