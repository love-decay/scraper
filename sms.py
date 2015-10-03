from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="(xxx) xxxxxxx", 
	from_="+1xxxxxxx", 
	body="ATTN:KimsufiSk10 available!",  
)
