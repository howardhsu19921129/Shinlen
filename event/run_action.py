import json
import sys
import os

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

def check_name_if_error(action_name, list_path): 
	load_data = get_json_data(list_path)
	for i in range (len(load_data['event_list'])):
		if load_data['event_list'][i]["name"] == action_name:
			if load_data['event_list'][i]["error"] == False:
				return False
			else:
				return True
	print("Can not find " + action_name)
	return True

def check_id_if_error(action_id, list_path):
	load_data = get_json_data(list_path)
	for i in range (len(load_data['event_list'])):
		if load_data['event_list'][i]["id"] == int(action_id):
			if load_data['event_list'][i]["error"] == False:
				return False
			else:
				return True
	print("Can not find id " + action_id)
	return True

def run_action_with_name(action_name, list_path):
	if not (check_name_if_error(action_name, list_path)):
		now_cd = os.getcwd()
		os.chdir('action_base')
		cmd = "python " + action_name
		os.system(cmd)
		os.chdir('../')
		print('action done')
	else:
		print("the file can not be found in base, action cancel")

def run_action_with_id(action_id, list_path):
	load_data = get_json_data(list_path)
	for i in load_data["event_list"]:
		if i["id"] == action_id:
			action_name = i["name"]
			now_cd = os.getcwd()
			os.chdir('action_base')
			cmd = "python " + action_name
			os.system(cmd)
			os.chdir('../')
			print('action done')
			return True

	print("no such id found")
	return False
	


print(check_name_if_error('action_example_6.py',"event_list.json"))
print(check_id_if_error(3,"event_list.json"))
run_action_with_id(2, "event_list.json")