
# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input

# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'
user_input = input("Hello")

while user_input != "Sensei I am at peace":
    user_input = input("Say something to mr miyagi ")

    if "Sensei" in user_input:
        if '?' in user_input:
            print('questions are wise, but for now. Wax on, and Wax off!')
        elif ("block" or "blocking") in user_input:
            print('Remeber, best block, not to be there..')
        else:
            print('do not lose focus. Wax on. Wax off.')
    else:
        print("You are smart, but not wise - address me as Sensei please")

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')