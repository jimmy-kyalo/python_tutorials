# defining a tuple
dimensions = (200, 0)
print(dimensions[0])
print(dimensions[1])

print('----------------------\n')


# looping thru variables in a tuple
dimensions = (200, 0)
for dimension in dimensions:
	print(dimension)

print('----------------------\n')

# writing over a tuple
dimensions = (200, 0)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)	
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)