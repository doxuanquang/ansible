import re
import os
import sys
import json

### import module
sys.path.insert(0, '/home/leo.do/ansible_example/python_files/module')
import all

path = os.path.dirname(os.path.abspath(__file__)) + '/pre/rp-acl/'

def open_file(path):
	a_dict = {}
	for file_name in os.listdir(path):
                file_path = path + file_name
		ip = file_name.split('_')[-1][:-4]
		a_dict[ip] = read_section(file_path)
	return all.sort_dict(a_dict)

def read_section(file_name):
        command_dict = {}
        main_line = ''
        with open(file_name, 'r') as f:
                lines = f.readlines()
                for i in range(0, len(lines) - 1):
                        if re.match(r'COMMAND:', lines[i]):
                                main_line = lines[i]
                                command_dict[lines[i]] = ''
                        else:
                                command_dict[main_line] += lines[i]
        return all.sort_dict(command_dict)

main_dict = open_file(path)
temp_dict = {}
for key in main_dict.keys():
	text = ''
	for sub_key in main_dict[key].keys():
		text += (sub_key + main_dict[key][sub_key])
#	print(text)
	if text not in temp_dict.keys():
		temp_dict[text] = key
	else:
		temp_dict[text] += (',' + key)

print(temp_dict)
device_name = ''
with open('rp-acl_pre.txt', 'w') as w:
	with open('inventory', 'r') as r:
		lines = r.readlines()
	for key in temp_dict.keys():
		w.write('*' * 50 + '\r\n' + key + '\r\nDevices (IP) with above output\r\n' + temp_dict[key] + '\r\n')
		for ip in temp_dict[key].split(','):
			for i in range (0, len(lines) - 1):
				if ip == lines[i].rstrip().strip():
					device_name += lines[i-1].rstrip().strip()[1:-1] + ','
		w.write('\r\nDevices (name) with above output\r\n' + device_name[:-1] + '\r\n' + '*' * 50 + '\r\n' * 3)





