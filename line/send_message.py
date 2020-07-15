import time
import requests
import json
import datetime
import sys

info_path = "info.json"
base_path = 'message_base.json'

def get_json_data(json_path):
	with open(json_path,'r') as f:  
		params = json.load(f)      
		dict = params  
		f.close()
	return dict

def print_dict(dict):
	for i in dict['message_base']:
		print(i)

def get_id_data_in_dict(input_dict,id):
	target = id
	for i in range(len(input_dict['message_base'])):
		if input_dict['message_base'][i]['id'] == target:
			return input_dict['message_base'][i]
	print("no such item")

def query_yes_no(message): #for final check
	yes = {'yes','y', 'ye', ''}
	no = {'no','n'}
	while True:
		choice = raw_input(message)
		if choice in yes:
			return True
		elif choice in no:
			return False
		else:
			sys.stdout.write("Please respond with 'yes' or 'no'")	

def sent_messsege_via_notify(message, info): #input 2 dict
	url = info['ip']
	LineNotifyToken = info['token']
	LineNotifyMessage = message['message']
	headers = {
			"Content-Type":"application/x-www-form-urlencoded",          
			"Authorization":"Bearer " + LineNotifyToken
		}
	body = "message=" + LineNotifyMessage
	result = requests.post(url, data = body, headers = headers)
	print 'Status Code = ' + str(result.status_code) + ', Response = ' + result.text


##main function

info_path = "info.json"
base_path = 'message_base.json'

print_dict(load_data)
select_id = int(raw_input("witch id do you want to sent?"))
info = get_json_data(info_path)
load_data = get_json_data(base_path)
print(get_id_data_in_dict(load_data,select_id))
sent_messsege_via_notify(get_id_data_in_dict(load_data,select_id), info)