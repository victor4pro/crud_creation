import sys
import csv

clients = [
	{
	'name': 'Pablo',
	'company': 'Google',
	'email': 'pablo@google.com',
	'position': 'software engineer'
	},
	{
	'name': 'Julio',
	'company': 'Facebook',
	'email': 'julio@facebook.com',
	'position': 'data engineer'
	}
	]

def create_client(client):
	global clients
	if client not in clients:
		clients.append(client)
	else:
		print('Client is already in the client\'s list')

def list_clients():
	global clients
	for idx, client in enumerate(clients):
		uid = idx
		name = client['name']
		company = client['company']
		email = client['email']
		position = client['position']
		print(f'{uid}  |  {name}  |  {company}  |  {email}  |  {position}')

def update_client(client_id):
	global clients
	if clients[int(client_id)]:
		client_updated = _get_client_data()
		clients[int(client_id)] = client_updated
	else:
		print("The client doesn't exist")

def delete_client(client_id):
	global clients
	if clients[int(client_id)]:
		position = clients.index(clients[int(client_id)])
		clients.pop(position)
	else:
		print("The client doesn't exist")

def _get_client_field(field):
	client_field = None

	while not client_field:
		client_field = str(input(f'What is the client {field}? : '))

		if client_field == 'exit':
			client_field = None
			break
	if not client_field:
		sys.exit()

	return client_field

def _get_client_data():
	client = {
		'name': _get_client_field('name'),
		'company': _get_client_field('company'),
		'email': _get_client_field('email'),
		'position': _get_client_field('position')
		}
	return client

def search_client(client_name):
	global clients
	for client in clients:
		if client['name'] == client_name:
			return True
			break
	return False


def _print_welcome():
	print('WELCOME TO SOFTWARE VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')
	print('[L]ist clients')

if __name__ == '__main__':
	_print_welcome()

	command = str(input()).lower()

	if command == 'c':
		client = _get_client_data()
		create_client(client)
		list_clients()
	elif command == 'u':
		client_id = _get_client_field('id')
		update_client(client_id)
		list_clients()
	elif command == 'd':
		client_id = _get_client_field('id')
		delete_client(client_id)
		list_clients()
	elif command == 's':
		client_name = _get_client_field('name')
		found = search_client(client_name)
		if found:
			print(f"The client {client_name} is in the client's list")
		else:
			print(f"The client {client_name} is not in the client's list")
	elif command == 'l':
		list_clients()		

	else:
		print('invalid command')
