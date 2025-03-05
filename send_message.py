import os
from twilio.rest import Client
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# defining auth variables and fetching them from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_number = os.getenv("WHATSAPP_NUMBER")

# adding the auth variables to client modular
client = Client(account_sid, auth_token)

# sending the message 
message = client.messages.create(
    from_ = 'whatsapp:+14155238886', 
    content_sid = 'HXb5b62575e6e4ff6129ad7c8efe1f983e',
    content_variables = '{"1":"12/1","2":"3pm"}',
    to = whatsapp_number
)

print message id to ensure it was sent
print(message.sid)