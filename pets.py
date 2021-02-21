pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#remove cat from the list
while 'cat' in pets:
	pets.remove('cat')
print()
#list only one instance of a pet
#list alphabetically
for pet in sorted(set(pets)):
	print(pet)
	print()

print('-------------------------------------------')

#positional arguments
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'fraizer')