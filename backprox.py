import requests
import time
import json
from twilio.rest import Client 
from credentials import *

URL1="http://cloud.boltiot.com/remote/api_key/digitalRead?pin=1&deviceName=bolt device name"
client = Client(account_sid, auth_token)

def sendsms():
	my_msg = "Alert!!! There is some suspicious activity near secure room - AutonMont."  
	message = client.messages.create(to=my_cell, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_1, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_2, from_=my_mobile, body=my_msg)
	message = client.messages.create(to=my_cell_3, from_=my_mobile, body=my_msg)

count=0
while True:
	r=requests.get(URL1)
	data=json.loads(r.text)
	print data['value']
	try:
		if(data['value']=='0'):
			count=count+1
		elif(data['value']=='1'):
			count=0	
		if(count>=20):
			sendsms()
			count=0
			
	except Exception as e:
		print "Error",e
				

		



