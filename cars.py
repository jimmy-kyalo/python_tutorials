class Car() :
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 500

	def description(self):
		new_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return new_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer) + " miles on it")

	def update_odometer(self, mileage):
		if mileage >= self.odometer:
			self.odometer = mileage
		else:
			print("You can't roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer += miles

class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = battery_size

	def decribe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		msg = "This car can go approximately " + str(range)
		msg += " miles on a full charge."
		print(msg)
	

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()


	def fill_gas_tank():
		print("This car doesn't need a gas tank")


