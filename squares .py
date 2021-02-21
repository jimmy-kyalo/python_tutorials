squares = [] #start an empty list
for value in range(1,11): #tell python to loop thru each value from 1 to 10
    square = value ** 2 #current value is raised to te second power and stored in the variable square
    squares.append(square) #each new value of square is appended to the list squares

print(squares)


#  ALSO
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

#   ALSO
squares = [value ** 2 for value in range(1,11)]
print(squares)