def make_pizza(size, *toppings):#asterisk make empty tuple and pack it
	#print list of requested toppings
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("-" + topping)


		