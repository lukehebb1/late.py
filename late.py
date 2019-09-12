from twilio.rest import Client
import sys, os

#account SID and auth token have been stored as environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#create twilio object
client = Client(account_sid, auth_token)

my_num = '+12028583669'
gf_num = '+353862259018'

#create and send message
message = client.messages.create(body="Hi, I'm really busy in college right now. I should be home by " + sys.argv[1], from_=my_num, to=gf_num)

print(message.sid)
