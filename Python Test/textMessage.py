#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = "AC29bbda4c65f809796bed13ca42cfd1f0"
authToken = "6f79e3f6dff1c10d6c8a2a7d2deaab38"
myNumber = '+841699516738'
twilioNumber = '+16282226738'

from twilio.rest import TwilioRestClient

def textmyself(message):
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

textmyself('(^_^) xin chao :). hihi :P')
