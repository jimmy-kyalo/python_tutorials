from cars import *

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.description())
my_beetle.update_odometer(500)
my_beetle.read_odometer()
print()
print('---------------------------------------')
print()
my_tesla = ElectricCar('tesla', 'cybertruck', 2020)
print(my_tesla.description())
my_tesla.battery.decribe_battery()
my_tesla.battery.get_range()

