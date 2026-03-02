# Dictionaries ---> Dicts organise data based on key/value pairs

# Dicts are mutable and dynamic

# Make a dictionary
my_dictionary = {
    "first_name": "Barak",
    "last_name": "Obama",
    "address": "17 Pennsylvania Ave."
}

# Get a value from a dict
print(my_dictionary["first_name"])

# Change a value in a dict
my_dictionary["address"] = "123 Main St."
print(my_dictionary["address"])

print(my_dictionary)

# Add a new key value pair
my_dictionary["job"] = "president"
print(my_dictionary)

# values and keys methods
print(my_dictionary.values())
print(my_dictionary.keys())

# Get key value pairs with items()
for keys, values in my_dictionary.items():
    print(keys, values)

# Delete a key/value pair
del my_dictionary["first_name"]
print(my_dictionary)