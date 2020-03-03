import datetime

name = "Lana"
last_name = ''
species = ''
eye_color = ''
hair_color =''
age = ''
date = datetime.datetime.now()

name = input("What new name would you like? ")
last_name = input("What new last name would you like? ")
eye_color = input("What new eye colour would you like? ")
hair_color = input("What new hair colour would you like? ")
age = int(input('Insert your age '))
year_of_birth = date.year-age

print(f"Hello {name} {last_name}! Welcome, your age is {age}, your eyes are {eye_color} and your hair color is {hair_color}.")
print(f"You said you we're {age} hence you were born in {year_of_birth}")

mothers_name = input("What is your mums name? ")
mothers_age = int(input("What is your mother's age? "))
date_diff = year_of_birth - (date.year - mothers_age)

print(f"your name is {name}, and you are {age} born on the year of {year_of_birth}. This is {date_diff} years later than {mothers_name} who was on on {date.year-mothers_age}")


