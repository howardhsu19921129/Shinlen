#!/usr/bin/python
import sys, os, json
import fnmatch

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
	for i in dict['dev_base']:
		print(i)

def find_last_event_id(dict): #find maximum id 
	max = 0
	for i in range(len(dict['event_list'])):
		if (dict['event_list'][i]['id'] > max):
			max = dict['event_list'][i]['id']
	return max

def add_new_discoverd(new_name, list_path):
	new_font = {
		"id":None,
		"name":new_name,
		"error":False
	}
	load_data = get_json_data(list_path) #import the json data
	new_font["id"] = find_last_event_id(load_data) + 1
	load_data['event_list'].append(new_font)
	write_json_data(load_data,list_path)

def mark_not_found_in_folder(unfound_name, list_path):
	load_data = get_json_data(list_path) #import the json data
	count = 0
	for i in range (len(load_data['event_list'])):
		if(load_data['event_list'][i]["name"] == unfound_name):
			count = i
	load_data['event_list'][count]["error"] = True
	write_json_data(load_data,list_path)



## main function
now_cd = os.getcwd()

# load the folder
folder_list = [f for f in os.listdir(now_cd + "/action_base") if fnmatch.fnmatch(f, '*.py')]

old_event_list = []
list_path = "event_list.json"
load_data = get_json_data(list_path)
for i in range (len(load_data['event_list'])): # load the list
	old_event_list.append(load_data['event_list'][i]["name"])

for item in folder_list: # find if any add
	if item not in old_event_list:
		add_new_discoverd(item, list_path)
		print("add "+ item + " in list")

for item in old_event_list: # find if any del
	if item not in folder_list:
		mark_not_found_in_folder(item, list_path)
		print("mark "+ item + " error")

print('list sync done')




