# xagrs
# method 1

def add(*numbers):
    print(numbers)

add(10,66,6655)

# method 2: sum all the numbers

def addi(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

addi(10,20,30,3,3,336)