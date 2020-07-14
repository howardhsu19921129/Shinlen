#!/usr/bin/python
import json
import sys

base_path = 'dev_base.json'

final_font = { #varibale that will be add to base
		"id":None,
		"name":"",
		"class":"", # should be "sensor" or "I/O"
		"enable":True, # should be True/False
		"status":{
			"RefreshTimeStamp":0, # should be int (time stamp)
			"lost":True, # should be True/False
			"error":False, # should be True/False
			"value":0 # should be 0 or 1 (or depend on class)
		}
	}


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

def write_json_data(dict, path): #
	with open(path,'w+') as r:
		json.dump(dict,r)       
	r.close()

def get_json_data(json_path):
	with open(json_path,'r') as f:  
		params = json.load(f)      
		dict = params  
		f.close()
	return dict

def find_last_dev_id(dict): #find maximum id 
	max = 0
	for i in range(len(dict['dev_base'])):
		if (dict['dev_base'][i]['id'] > max):
			max = dict['dev_base'][i]['id']
	return max

load_data = get_json_data(base_path) #import the json data
final_font['id'] = find_last_dev_id(load_data) + 1
final_font['name'] = raw_input('name: ')

final_font['class'] = raw_input('class("sensor" / "I/O"): ')
while ((final_font['class'] != 'sensor') and (final_font['class'] != 'I/O')):
	print("Format must be wrong")
	final_font['class'] = raw_input('class("sensor" / "I/O"): ')

enable_select = query_yes_no("enable the dev? [y/n]")
if not enable_select:
	final_font['enable'] = False

print("is this the message you want to import?") # final check
print(final_font)
final_check = query_yes_no("[y/n]")

if final_check: #after final check
	load_data['dev_base'].append(final_font)
	try:	
		write_json_data(load_data,base_path)
		print("add dev done")
	except:
		print("unexpected error")
else:
	print("Cancel adding dev")



