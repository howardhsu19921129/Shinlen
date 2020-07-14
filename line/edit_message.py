import json
import sys
base_path = 'message_base.json' #path to the message base

edit_item = {1:"message", 2:"receiver_type", 3:"receiver"}

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
	for i in dict['message_base']:
		print(i)  

def get_id_data_in_dict(input_dict,id): #return dict if exist, return None if not exist
	target = id
	for i in range(len(input_dict['message_base'])):
		if input_dict['message_base'][i]['id'] == target:
			return input_dict['message_base'][i]


def get_id_order_in_dict(input_dict,id):
	target = id
	for i in range(len(input_dict['message_base'])):
		if input_dict['message_base'][i]['id'] == target:
			return i

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


load_data = get_json_data(base_path) #import the json data
print_dict(load_data)

select_id = int(raw_input("which id do you want to edit? "))
select_data = get_id_data_in_dict(load_data,select_id)
select_data_order = get_id_order_in_dict(load_data,select_id)
if select_data != None:
	print(edit_item)
	select_item = int(raw_input("which item do you want to edit? "))
	if (1 <= select_item <= 3):
		new_data = raw_input("Plz enter new data : ")

		if (select_item == 1): #edit message
			load_data['message_base'][select_data_order][edit_item[select_item]] = new_data

		elif(select_item == 2): #edit receiver type
			while ((new_data != 'building') and (new_data != 'groups') and (new_data != 'user')):
				print("Format must be wrong, it should be building/groups/user")
				new_data = raw_input("Plz enter new data : ")
			load_data['message_base'][select_data_order][edit_item[select_item]] = new_data

		elif(select_item == 3): #edit receiver
			load_data['message_base'][select_data_order][edit_item[select_item]] = change_to_list(new_data)

		else:
			print('unexpected err in select item')

		print(print_dict(load_data))
		
		#write data here
	else:
		print("The id is not exist")    

else:	
	print("The id is not exist")

