# for loops

# syntax

# for item in iterable:
    # block of code to item

cool_cars = ['Skoda felicia fun', 'Fiat abarth the old one', 'toyota corola','Fiat panda 4 x 4', 'Fiat Multipla']

count = 0
for car in cool_cars:
    print(count, '-', car)
    count += 1



# looping with dictionary
boris_dict = {
    'name': 'Boris',
    'l_name': 'Johnson',
    'phone': '0784171157',
    'address': '10 downing street'
}

for key in boris_dict:
    print(key)

print(boris_dict['phone'])

for key in boris_dict:
    print(boris_dict['phone'])
    print(boris_dict['name'])