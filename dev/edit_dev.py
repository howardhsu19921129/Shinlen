import json
import sys
from distutils.util import strtobool

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

def print_dict(dict):
	for i in dict['dev_base']:
		print(i)

def get_id_data_in_dict(input_dict,id): #return dict if exist, return None if not exist
	target = id
	for i in range(len(input_dict['dev_base'])):
		if input_dict['dev_base'][i]['id'] == target:
			return input_dict['dev_base'][i]

def get_id_order_in_dict(input_dict,id):
	target = id
	for i in range(len(input_dict['dev_base'])):
		if input_dict['dev_base'][i]['id'] == target:
			return i

def check_if_is_number(input):
	try:
		new_data = int(input)
		return True
	except:
		return False

def check_if_is_bool(input):
	yes = ("yes", "true", "t", "1")
	no = ("no", "false", "f", "0")
	if (input.lower() in yes) or (input.lower() in no):
		return True
	else:
		return False

def convert_str_to_bool(input):
	yes = ("yes", "true", "t", "1")
	if (input.lower() in yes):
		return True
	else: 
		return False

def edit_status(status):
	status_item = {0:"RefreshtimeStamp",1:"lost", 2:"error", 3:"value"}
	print(status_item)
	select_item = int(raw_input("which item do you want to edit? "))
	if (0 <= select_item <= 3):
		new_data = raw_input("Plz enter new data : ")
		if (select_item == 0): #edit timeStamp
			while (not check_if_is_number(new_data)):
				new_data = raw_input("new data should be number: ")
			status[status_item[select_item]] = int(new_data)

		elif (select_item == 1): #edit 'lost'
			while (not check_if_is_bool(new_data)):
				print("'lost' should be true or false")
				new_data = raw_input("Plz enter new data : ")
			status[status_item[select_item]] = convert_str_to_bool(new_data)

		elif (select_item == 2): #edit 'error'
			while (not check_if_is_bool(new_data)):
				print("'lost' should be true or false")
				new_data = raw_input("Plz enter new data : ")
			status[status_item[select_item]] = convert_str_to_bool(new_data)

		elif (select_item == 3): #edit 'value'
			while (not check_if_is_number(new_data)):
				new_data = raw_input("new data should be number: ")
			status[status_item[select_item]] = int(new_data)                    
		else:
			print('unexpected err in select item')

		return status



base_path = 'dev_base.json' #path to the message base
edit_item = {0:"enable",1:"name", 2:"class", 3:"status"}
load_data = get_json_data(base_path) #import the json data
print_dict(load_data)

select_id = int(raw_input("which id do you want to edit? "))
select_data = get_id_data_in_dict(load_data,select_id)
select_data_order = get_id_order_in_dict(load_data,select_id)
if select_data != None:
	print(edit_item)
	select_item = int(raw_input("which item do you want to edit? "))
	if (0 <= select_item <= 2):
		new_data = raw_input("Plz enter new data : ")

		if(select_item == 0): # edit enable
			while (not check_if_is_bool(new_data)):
				print("'enable' should be true or false")
				new_data = raw_input("Plz enter new data : ")
			load_data['dev_base'][select_data_order][edit_item[select_item]] = convert_str_to_bool(new_data)

		elif(select_item == 1): # edit name
			load_data['dev_base'][select_data_order][edit_item[select_item]] = new_data

		elif(select_item == 2): # edit class ('sensor' or 'I/O')
			while (new_data.lower() != 'sensor') and (new_data.lower() != 'i/o'):
				print("'class' should be sensor or I/O")
				new_data = raw_input("Plz enter new data : ")
			load_data['dev_base'][select_data_order][edit_item[select_item]] = new_data.lower()

		else:
			print('unexpected err in select item') 

		#write data here
		try:	
			write_json_data(load_data,base_path)
			print("edit dev done")
		except:
			print("unexpected error")	

	elif(select_item == 3): # edit status
		load_data['dev_base'][select_data_order][edit_item[select_item]] = edit_status(load_data['dev_base'][select_data_order][edit_item[select_item]])
		
		try:	
			write_json_data(load_data,base_path)
			print("edit dev done")
		except:
			print("unexpected error")	
	else:
		print('unexpected err in select item')
