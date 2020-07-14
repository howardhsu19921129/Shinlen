#!/usr/bin/python
import json
import sys
import os
action_list = {0:"list_message",1:"send_message", 2:"add_message", 3:"del_message", 4:"edit_message", "exit":"exit"}
print("start message service")
cmd = "python list_message.py"
while(True):
    print("please select : ")
    select_action = raw_input(str(action_list) + ": " )
    print(select_action)
    if(select_action == 'exit'):
        break
    else:
        if(select_action == '0'):
            cmd = "python list_message.py"
            os.system(cmd)
        elif(select_action == '1'):
            cmd = "python send_message.py"
            os.system(cmd)
        elif(select_action == '2'):
            cmd = "python add_message.py"
            os.system(cmd)
        elif(select_action == '3'):
            cmd = "python del_message.py"
            os.system(cmd)
        elif(select_action == '4'):
            cmd = "python edit_message.py"
            os.system(cmd)
        else:
            print('your select may be wrong.')

        select_action = None