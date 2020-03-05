
# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

number = ""

while number != "penpinapplespen":
    number = int(input("Enter a number: "))

    temp_num = number
    number = 1
    while number <= temp_num:
        print(number)
        number += 1
        if number % 3 == 0 and number % 5 == 0:
            print('boringbuzz')
        elif number % 3 == 0:
            print('boring')
        elif number % 5 == 0:
            print('buzz')