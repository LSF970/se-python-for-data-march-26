# Consolidating the basics of Python

import sys

# Variables
x = 10 # Int
name = "Luke" # Str
is_happy = True # Bool

# Using Variables
print("Hello")
print(name)
print("Are you happy?", is_happy)
print(x)
print(type(name)) # str

# Reassigning values
x = 20
print("Now x is:", x)

# Memory concept
my_number = 5
print(my_number)

my_number = my_number + 3
print(my_number)

# Types - int, floats, str, bool
# Integer
num_1 = 1
print(num_1)
print(type(num_1))        # <class 'int'>
print(sys.getsizeof(num_1))

# Float
float_1 = 1.00
print(type(float_1))      # <class 'float'>
print(sys.getsizeof(float_1))

# String
str_1 = '1'
print(type(str_1))        # <class 'str'>
print(sys.getsizeof(str_1))

# Boolean
bool_1 = True  # note: must be capitalised
print(type(bool_1))       # <class 'bool'>
print(sys.getsizeof(bool_1))

# Casting
my_num = 5 # Int
my_float = float(my_num)
print(my_float)

my_str = "123"
my_int = int(my_str)
print(my_int)

# User input
user_number = int(input("Enter a number between 1 and 20:"))
print("Your number is:", user_number)
print(type(user_number))