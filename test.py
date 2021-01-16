from twilio.rest import Client 
import config

account_sid = config.account_sid
auth_token = config.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18189462554',
    body ='jazz hands',
    to='+17809530388'
)