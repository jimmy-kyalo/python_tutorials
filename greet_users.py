def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "."
		print(msg)

usernames = ['jimmy', 'john', 'ann']
greet_users(usernames)