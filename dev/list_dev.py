#!/usr/bin/python
import json
import sys

def get_json_data(json_path):
	with open(json_path,'r') as f:  
		params = json.load(f)      
		dict = params  
		f.close()
	return dict

def print_dict(dict):
	for i in dict['dev_base']:
		print(i)

def list_message():##main function
	base_path = 'dev_base.json' 
	load_data = get_json_data(base_path)
	print_dict(load_data)

list_message()