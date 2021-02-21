from cars import Car

my_new_car = Car('toyota', 'prado' , 2018)
print(my_new_car.description())

my_new_car.update_odometer(23)
my_new_car.read_odometer()