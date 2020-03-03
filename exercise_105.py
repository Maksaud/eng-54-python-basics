# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: .sort()

some_thing = [1, 2, 3, 4, 5]

# Print the lists and check it's type
print(some_thing)
print(type(some_thing))

# Print the list's first object
print(some_thing[0])

# Print the list's second object
print(some_thing[1])

# Print the list's last object
print(some_thing[4])

# Re-define the first item on the list and
some_thing[0] = 6

# Re-define another item on the list and print all the list
some_thing[1] = 7
print(some_thing)

# Add an item to the list and print the list
some_thing.append(9)

# Remove an item from the list and print the list
some_thing.pop(4)
print(some_thing)

# Add two items to list and print the list
some_thing.append(10)
some_thing.append(11)