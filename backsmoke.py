import requests
import time
import json
from twilio.rest import Client 
from credentials import *

URL1="http://cloud.boltiot.com/remote/api_key/analogRead?pin=A0&deviceName=bolt device name"
client = Client(account_sid, auth_token)

def sendsms():
	my_msg = "Alert!!!!!!!!!!! There is a FIRE in the plant!!!! - AutonMont."  
	message = client.messages.create(to=my_cell, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_1, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_2, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_3, from_=my_mobile, body=my_msg)


while True:
	r=requests.get(URL1)
	data=json.loads(r.text)
	print int(data['value'])
	try:
		if(int(data['value'])>1000):
			sendsms()
			time.sleep(20)
			
	except Exception as e:
		print "Error",e
				

		



