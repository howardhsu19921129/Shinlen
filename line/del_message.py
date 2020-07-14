#!/usr/bin/python
import json
import sys
base_path = 'message_base.json' 

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

def get_json_data(json_path):
	with open(json_path,'r') as f:  
		params = json.load(f)      
		dict = params  
		f.close()
	return dict

def write_json_data(dict, path): #
	with open(path,'w+') as r:
		json.dump(dict,r)       
	r.close()

def print_dict(dict):
	for i in dict['message_base']:
		print(i)

def get_id_data_in_dict(input_dict,id):
	target = id
	for i in range(len(input_dict['message_base'])):
		if input_dict['message_base'][i]['id'] == target:
			return input_dict['message_base'][i]
	print("no such item")

    
##main function
load_data = get_json_data(base_path)
print_dict(load_data)
select_id = int(raw_input("witch id do you want to remove?"))
select_data = get_id_data_in_dict(load_data,select_id)
if select_data != None:

	if query_yes_no("is this the message you want to remove? y/n"):
		load_data["message_base"].remove(select_data)
		try:
			write_json_data(load_data, base_path)
			print("The messege has been removed")
		except:
			print("unexpected error")

	else:
		print("Cancel del message")
else:
	print("The id is not exist")