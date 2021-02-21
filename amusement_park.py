"""For example, consider an amusement park that charges different rates for
different age groups:
-Admission for anyone under age 4 is free.
-Admission for anyone between the ages of 4 and 18 is $5.
-Admission for anyone age 18 or older is $10.
How can we use an if statement to determine a person’s admission rate?
The following code tests for the age group of a person and then prints an
admission price message:"""

age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")	
else:
	print("Your admission cost is $10.")	