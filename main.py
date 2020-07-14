#!/usr/bin/python
import json
import sys
def start_message_service():
	sys.path.append(sys.path[0] + "/line")
	print(sys.path)
	from sys.path.line import main_message_service
	



while True:
	action_list = {1:"dev_service", 2:"message_service", 3:"event_service"}
	print("please enter the action number")
	print(str(action_list))
	service_select = int(raw_input())

	if (service_select == 1): #in dev service
		print('you select 1')

	elif (service_select == 2): #in message service
		print('you select 2')
		start_message_service()

	elif (service_select == 3): #in event service
		print('you select 3')

	else:
		print('you have a wrong input')
