num1 = {1,2,3}
num2 = set([4,5,6])

# function for set
num2.add(7)
num2.remove(7)
num1.clear()
print(num1)
print(num2)
print(7 in num2)

# operation in set
print(num1 | num2) #union between two sets
print(num1 & num2) #intersection between two sets
