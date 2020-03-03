# Strings
# text and characters
# Syntax
# "" and ''

# Define a string
my_string = 'Hey I am a cool string B) '
print(my_string)

# check its type
print(type(my_string))

# concatenation
# Adding two strings
#joint_string = my_string + 'This is another string'
#print(joint_string)
# example 2 of concatination
#name = 'Mohammed'
#welcome_text = 'WELCOME TO SPARRRRRTTAAAAA (300)'
#print( welcome_text + ' ' + name)
#print(welcome_text, name)# overoading the print method

# interpolation
# inserting a string inside another string
# or running python inside a string
#print(f'WELCOME {name} TO CLASS 54, we are Contested Terrain')
#print('WELCOME {} TO CLASS 54, we are Contested Terrain'.format(name))



# usefull methods
# are like functions byt belong to a specific data type
# for example, it would not make sense to try to capitalize integers.
example_long_string = '    HELLO, THis is a very BAdly formated text?    '


# remove trailling white spaces
print(example_long_string.strip())
# Make it lower case
print(example_long_string.lower())

# make it upper case
print(example_long_string.upper())
# make only the first char capitalised
print(example_long_string.strip().capitalize())

# make first of each capitalised
print(example_long_string.title())

# change question mark into a '!'
print(example_long_string.replace('?', '!'))
# chain some methods and:
    # remove trailing white spaces
    # make it nicely formated wth only the first letter capitalised
print(example_long_string.strip().capitalize())

print(example_long_string.split())