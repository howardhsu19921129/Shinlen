#!/usr/bin/python
import json
import sys
base_path = 'message_base.json' #path to the message base
final_font = { #varibale the will be add to base
		"id":None,
		"message":"",
		"receiver_type":"",
		"receiver":[]
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

def find_last_id(dict): #find maximum id 
	max = 0
	for i in range(len(dict['message_base'])):
		if (dict['message_base'][i]['id'] > max):
			max = dict['message_base'][i]['id']
	return max

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

def change_to_list(input): # use to turn 'receiver' input into a list
	new_list = list()
	blank = 0
	for i in input:
		if((i != ',') and (i != ' ')):
			try:
				new_list[blank] = new_list[blank] + i
			except:
				new_list.append('')
				new_list[blank] = new_list[blank] + i
		else:
			blank = blank + 1
	return new_list

## main function 
load_data = get_json_data(base_path) #import the json data
final_font['id'] = find_last_id(load_data) + 1 
final_font['message'] = raw_input('message: ')
final_font['receiver_type'] = raw_input('receiver_type(building/groups/user): ')
while ((final_font['receiver_type'] != 'building') and (final_font['receiver_type'] != 'groups') and (final_font['receiver_type'] != 'user')):
	print("Format must be wrong")
	final_font['receiver_type'] = raw_input('receiver_type(building/groups/user): ')
	print(final_font['receiver_type'])

final_font['receiver'] = change_to_list(raw_input('receiver: ')) #has to be a list

print("is this the message you want to import?") # final check
print(final_font)
final_check = query_yes_no("[y/n]")

if final_check: #after final check
	load_data['message_base'].append(final_font)
	try:	
		write_json_data(load_data,base_path)
		print("add message done")
	except:
		print("unexpected error")
else:
	print("Cancel adding message")