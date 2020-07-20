import sys, os, json

def get_json_data(json_path):
	with open(json_path,'r') as f:  
		params = json.load(f)      
		dict = params  
		f.close()
	return dict

def list_action(list_path):
	load_data = get_json_data(list_path)
	for i in load_data['event_list']:
		print(i)


list_path = 'event_list.json' 
list_action(list_path)
