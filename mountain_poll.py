responses = {}

#set active flag
poll_active = True

while poll_active:
	name = input("\nWhat is your name? ")
	response = input("\nWhich mountain would you like to climb? ")

	#store the response in the dict
	responses[name] = response

	#find out if anyone else will take poll
	repeat = input("\nAnyone else? (yes/ no) ")
	if repeat == 'no':
		poll_active = False

print("\n-----Poll Results-----")
print()
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + '.')
	print()