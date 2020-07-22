import json, sys, os
import dictdiffer

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

def find_change(new_base,cache_base):
	if (new_base == cache_base):
		print("no dev has change")
		return []
	else:
		change_list = []
		changes = {"id":None}
		for i in new_base["dev_base"]:
			for j in cache_base["dev_base"]: 
				if j["id"] == i["id"]:
					temp  = list(dictdiffer.diff(i["status"], j["status"]))
					if len(temp) != 0:
						for count in range(len(temp)):
							changes["id"]=(i["id"])
							changes[temp[count][1]] = temp[count][-1][0]
							change_list.append(changes)
							changes = {"id":None} # clear temp
		return change_list

def check_trigger_action(change_report, trigger_list_path):

	keys = change_report.keys()
	keys.remove("id")

	dev_id = change_report["id"]
	dev_item = keys[0]
	item_value = change_report[dev_item]

	# get auto_trigger_list
	auto_trigger_list = get_json_data(trigger_list_path)

	for i in auto_trigger_list["auto_trigger_list"]:
		if dev_id == i["dev_id"]:
			if dev_item == i["dev_item"]:
				if i["enable"]:
					if (type(item_value) == type(i["item_value"])):
						if(item_value == i["item_value"]):
							trigger_id = i["trigger_id"]
							return trigger_id
	
	return False

def run_action_with_id(action_id, list_path):
	load_data = get_json_data(list_path)
	for i in load_data["event_list"]:
		if i["id"] == action_id:
			action_name = i["name"]
			now_cd = os.getcwd()
			os.chdir('../')
			os.chdir('event/action_base')
			now_cd = os.getcwd()
			cmd = "python " + action_name
			os.system(cmd)
			os.chdir('../')
			print('action done')
			return True

	print("no such id found")
	return False

## get new data & cache data
org_path = os.getcwd()
cache_path = org_path + '/dev_cache.json'
os.chdir('../')
os.chdir('dev')
now_cd = os.getcwd()
base_path = now_cd + '/dev_base.json'
os.chdir('../')
os.chdir('event')
now_cd = os.getcwd()
list_path = now_cd + '/event_list.json'

cache_data = get_json_data(cache_path)
load_data = get_json_data(base_path) 
os.chdir(org_path)

## out put different
change_report = find_change(load_data, cache_data)

trigger_list_path = "auto_trigger_list.json"
for i in range(len(change_report)):
	action_id = check_trigger_action(change_report[i], trigger_list_path)
	run_action_with_id(action_id,list_path)

# ##rewrite cache data
cache_data = load_data
write_json_data(cache_data, cache_path)