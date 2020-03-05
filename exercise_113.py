#functions
# practice using, defining and calling functions
# Build a basic object functional
# phase1: build function containing add, subtract, multiply divide

# calculate the area of a circle
# calculate the area of a square
# calculate the area of a triangle (just find the easiest way)

def add_function(num1, num2):
    return num1 + num2

# As a user I want to have a add_function()
# that takes in two arguments and add them.

print("calling the add_function() with 290 and 10, expect 300 to be the result ")
print(add_function(290, 10) == 300)
print('got:', add_function())

print("calling the add_function() with 270 and 5, expect 275 to be the result ")
print(add_function(270, 5) == 275)
print('got:', add_function(270, 5))

def subtract_function(num1, num2):
    return num1 - num2

print(subtract_function(290, 10) == 280)

def multiply_function(num1, num2):
    return num1 * num2

print(multiply_function(290, 10) == 2900)

def divide_function(num1, num2):
    return num1 / num2

print(divide_function(290, 10) == 29)

def circle(num1):
    return 3.14 * num1**2

print(circle(5) == 78.75)


def square(num1):
    return num1*num1

print(square(5) == 25)

def triangle(num1, num2):
    return (num1*num2)/2

print(triangle(5, 5) == 12.5)

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(9))