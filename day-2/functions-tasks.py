# Functions tasks

# Task 1 - Basic Function
def my_first_function(thing):
    print(f"I love {thing}!")

my_first_function("Python")
my_first_function("Coffee")

# Task 2 - Tripler function
def tripler(num):
    return num * 3

print(tripler(2))
print(tripler(10))
print(tripler(-4))

# Task 3 - Greeter function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# Task 4 - Even or Odd function
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))  # Even
print(is_even(7))   # Odd

# Task 5 - Word Multiplier function
def repeat_word(word, times):
    return word * times

print(repeat_word("Hi", 3))   # HiHiHi
print(repeat_word("Wow", 5))  # WowWowWowWowWow

# Task 6 - Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120
print(factorial(3))  # 6

# Task 7 - Default params function
def power(base, exponent=2):
    return base ** exponent

print(power(4))     # 16 (4 squared) 4x4
print(power(2, 3))  # 8 --> 2x2x2
print(power(2, 5))  # 32 --> 2x2x2x2x2