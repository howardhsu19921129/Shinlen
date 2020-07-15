#!/usr/bin/python
import json
import sys
import os
def start_dev_service():
	now_cd = os.getcwd()
	os.chdir('dev')
	cmd = "python _main_dev_service.py"
	os.system(cmd)
	os.chdir('../')
	print('dev_service stop')

def start_message_service():
	now_cd = os.getcwd()
	os.chdir('line')
	cmd = "python _main_message_service.py"
	os.system(cmd)
	os.chdir('../')
	print('message_service stop')

def start_event_service():
	now_cd = os.getcwd()
	os.chdir('event')
	cmd = "python _main_event_service.py"
	os.system(cmd)
	os.chdir('../')
	print('event_service stop')

while True:
	action_list = {1:"dev_service", 2:"message_service", 3:"event_service", "exit":"exit"}
	print("please select the action number")
	service_select = raw_input(str(action_list) + ": " )
	if(service_select == 'exit'):
		break
	else:
		if(service_select == '1'):
			start_dev_service()

		elif(service_select == '2'):
			start_message_service()

		elif(service_select == '3'):
			start_event_service()
	
		else:
			print('your select may be wrong.')