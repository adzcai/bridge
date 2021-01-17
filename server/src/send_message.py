# Import Libraries
from twilio.rest import Client
import config

# Initialize Twilio client configuration
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

# Send Message
def send_message():
    message = client.messages.create(
        from_=config.Twilio_number,
        body='Thank you for choosing Bridge, you can learn more about this service by using the command !help',
        to=config.reciever
    )

send_message()