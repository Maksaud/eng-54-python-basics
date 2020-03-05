# Functions
# A function is like a machine,
# it can take in inputs and do some work (block of code)
# it can output code
# do something different
# They need to be called

# Calling a function is just writing the name and passing the arguments

# functions
# they do one job
# They should be testable and maintainable
# they should have good naming convention
# Generay never prints inside a functions

# ### the above avoid stringy code - Spaguetti code
# Reduce technical debt
# concept of DRY
# Don't
# repeat
# yourself

# Seperation of concerns
# you separate logically your code.
# place where you define functions
# place where you run functions
# place where you write tests
# place where you define seeds (seeds are fake data for your app)



# Syntax
def name_of_function(arg1, arg2):
    # block of code
    return 'doing some work'

def say_hello_zeus(x):
    x = "hello zues"
    return x

# calling AND printing a function
print(say_hello_zeus())

say_hello_zeus()
'hello zeus'
# function with


# function with arguments
def full_name_formater(f_name, l_name):
    formated_f_name = f_name.strip().capitalize()
    formated_l_name = l_name.strip().capitalize()
    # format each name nicely
    # I can use .strip and .capitalised
    # I have acccess to the name via the arguments f_name and l_name
    # save thses into variables

    # return a joined full name that is correctly formatted
    # join the two variable into one string
    # return said string
    full_name = formated_f_name + formated_l_name
    return full_name


print(full_name_formater(' SHAnnon  ', '     GreyhOUnd'))

def add_funct(num1, num2):
    # I want to return two numbers
    # access to num1 and num 2 I can add them
    # I can save result in a variable
    result = num1 + num2
    # I can return said variable
    return result

print(add_funct(10, 300))