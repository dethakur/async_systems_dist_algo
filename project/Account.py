import json




variable = open('project/sample.json')
x = variable.read()
sample = json.loads(x)


#print(sample['config'])
for el in sample['config']:
	print(el['bank_name'])
	for clients in el['clients']:
		print(clients)

