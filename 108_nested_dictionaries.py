# nest data structures

crazy_landl_1 = {
    'name': 'Boris',
    'phone': '12345678910',
    'address_of rent': '10 Chelsea',
    'age': 55

}

crazy_landl_2={
    'name': 'Filipe',
    'phone': '12345678910',
    'address_of_rent': 'Comporta, Portugal',
    'age': 28
}

nested_dictionary = {
    'boris': crazy_landl_1,
    'filipe': crazy_landl_2
     }
#
# print(nested_dictionary)
#
# for key in nested_dictionary:
#     print(key)
#     data_nested = nested_dictionary[key]
#     print(data_nested)
#     print(type(data_nested))
#     print(data_nested.keys())
#     print(data_nested['name'])
#     print(data_nested['address_of_rent'])

nested_list = [[1, 2, 3],[4, 5, 6]]

print(nested_list[0])
print(nested_list[1])
print(nested_list[1][0])


for data in nested_list:
    print(data)
    for num in data:
        print(num * 20)
