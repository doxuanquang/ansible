import os

path ="/home/leo.do/ansible_example/gs_ny4_expansion_q2_2019/QA/results/show_vlan_br"
name = ''
with open('inventory', 'r') as f:
        lines = f.readlines()
	for file in os.listdir(path):
		ip = file.split('_')[-1][:-3]
		for i in range (0, len(lines) - 1):
			if ip in lines[i]:
				name = line[i-1][1:-1]
	        		os.rename(path + file, name)
