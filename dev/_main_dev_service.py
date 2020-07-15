#!/usr/bin/python
import json
import sys
import os
action_list = {0:"list_dev", 1:"add_dev", 2:"del_dev", 3:"edit_dev", "exit":"exit"}
print("start dev service")
cmd = "python list_dev.py"
while(True):
	print("please select : ")
	select_action = raw_input(str(action_list) + ": " )
	print(select_action)
	if(select_action == 'exit'):
		break
	else:
		if(select_action == '0'):
			cmd = "python list_dev.py"
			os.system(cmd)
		elif(select_action == '1'):
			cmd = "python add_dev.py"
			os.system(cmd)
		elif(select_action == '2'):
			cmd = "python del_dev.py"
			os.system(cmd)
		elif(select_action == '3'):
			cmd = "python edit_dev.py"
			os.system(cmd)
		else:
			print('your select may be wrong.')
		select_action = None