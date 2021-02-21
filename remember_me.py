import json

def get_stored_username():
	#get stored name, if available
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	#prompt for a new username
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	#greet user by name
	username = get_stored_username()
	if username:
		print("Welcome back, " + username.title())
		
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username.title())

greet_user()
