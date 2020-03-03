# practice string
# welcome to sparta

# version 1 specs
# define a variable name, and assign a string with a name
name = "Hello my name is maksaud"

# prompt the user for input and ask the user for his/her name
# re assign the original variable with the input
name = input("What is your name? ")

# use concatination to print a welcome message and use method to format the name/input
print("hello {}, how are you today?".format(name))


# version2
# ask the user for a first name, save it in a variable
first_name = input("What is your first name? ")

# ask the user for a last name, save it in a variable
last_name = input("What is your second name? ")

# use interpoation to print the message
print(f"Hello {first_name} {last_name}, How are you today?")

# do the same but use a different message and
number1 = input("Input first number: ")
number2 = input("Input second number: ")

# use interpolation to print the message
print(f"the sum of {number1} and {number2} id {int(number1) + int(number2)}")

# ints
person_name = input("Input your name: ")
age = input("Input your age: ")

print(f"nice, you were born in {2020 - int(age)}")