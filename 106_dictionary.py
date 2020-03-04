# Dictionary
# Dictionaries work with key and value pairs
# Work like a real dictionary, just lookup the information for the specific key.
# The big difference with list is they are organised with indexes and here we use keys.

# We just make a list of cring_landlords, but we need more infor like phone numbers and addresses.

# Syntax\boris
dict_variable_name = {'key': 'value'}

boris_dict = {
    'name': 'Boris',
    'l_name': 'Johnson',
    'phone': '0784171157',
    'address': '10 downing street'
}

print(boris_dict)
print(type(boris_dict))

# Access one key value pair
# follow the same principle of a list, but, use keys not indexes
print(boris_dict['name'])
last_name = boris_dict['l_name']
print(last_name)

# change the value of one key value pair
boris_dict['phone'] = '+7 9374749933'
print(boris_dict['phone'])

# Assign a new key value pair
boris_dict['home_phone'] = '+44 43234565421'
print(boris_dict['home_phone'])
print(boris_dict)

boris_dict['number_budgets_passed'] = 0
print(boris_dict)
boris_dict['number_budgets_passed'] += 1
print(boris_dict)
boris_dict['number_budgets_passed'] += 1
print(boris_dict)


# get all the key
print(boris_dict.keys())


# get all the values
print(boris_dict.values())

# nested structures