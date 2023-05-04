from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
from twilio.base.exceptions import TwilioRestException

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "Your message goes here..."

print(my_cell)

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)


try:
  message = client.messages.create(to="+12316851234", from_="+15555555555",
                                   body="Hello there!")
except TwilioRestException as e:
  print(e)