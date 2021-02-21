#!/usr/bin/python3
class Dog():
	#a simple attempt to model a dog
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting")

	def roll_over(self):
		print(self.name.title() + " rolled over")

#multiple instances
my_dog = Dog('fraizer', 3)
your_dog = Dog('rex', 6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old")
my_dog.sit()

print()

print("Your dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.roll_over()