# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# We should define/assign number to a variable called magic_number
magic_number = 5
count = 6
while(count != 0):
    # I need to ask user for input
    user_number = int(input('What is your chosen number between 0 and 10 '))


    # I need to check if this input matches a magic_number
    if magic_number == user_number:
        print('You are correct')
        break
    else:
        print(f"You were wrong, You have {count} turns left")
        count = count-1
        continue


    # I need to let the user know if the response was write or not
    #self five