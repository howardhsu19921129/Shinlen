#!/usr/bin/python
import json
import sys
import os
action_list = {0:"list_event", 1:"add_event", 2:"del_event", 3:"edit_event", "exit":"exit"}
print("start event service")
cmd = "python list_event.py"
while(True):
    print("please select : ")
    select_action = raw_input(str(action_list) + ": " )
    print(select_action)
    if(select_action == 'exit'):
        break
    else:
        if(select_action == '0'):
            cmd = "python list_event.py"
            print('run ' + cmd)
            #os.system(cmd)
        elif(select_action == '1'):
            cmd = "python send_event.py"
            print('run ' + cmd)
            #os.system(cmd)
        elif(select_action == '2'):
            cmd = "python add_event.py"
            print('run ' + cmd)
            #os.system(cmd)
        elif(select_action == '3'):
            cmd = "python del_event.py"
            print('run ' + cmd)
            #os.system(cmd)
        else:
            print('your select may be wrong.')
        select_action = None