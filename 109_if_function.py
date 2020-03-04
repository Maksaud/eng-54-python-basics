# functions
# syntax
# if <condition>:
    # block of code

# elif <condition>:
    # block of code that runs if return true

# else:
    # block of code that runs when all OTHER CONDITIONS ARE FALSE


# Notes:
# if functions will exit once a condition becomes true
# build your if functions with the most specific thing at the top.c


weather = 'rainy'

if weather == 'rainy':
    print('take your umbrella')
elif weather == 'sunny':
    print('nice, take some shades B) ')
else:
    print("Didn't quit catch that sport, could you repeat")


## Reads whatever is inside a variable and checks if it matches.

if 'rainy' in weather:
    print('take your umbrella')
elif 'sunny' in weather:
    print('nice, take some shades B) ')
else:
    print("Didn't quit catch that sport, could you repeat")