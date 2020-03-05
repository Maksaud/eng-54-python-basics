age = 19
driving_license = True
# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!
user_input = input('Do you want to exit')
if age >= 19 and driver_lisence:
    print('You can vote and drive,')
elif age >= 19 and driver_lisence:
    print("you can vote")
elif driver_lisence:
    print("You can drive")
elif 19 < age >= 16:
    print("You can leagally drink but your mates/uncles might have your back")
else:
    print("Your too young, go back to school!")

 #  as a user I should be able to keep being prompted for input until I say 'exit'