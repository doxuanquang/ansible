with open('inventory', 'w+') as w:
	for i in range (1,75):
		w.write('10.29.32.' + str(i) + '\r\n')
