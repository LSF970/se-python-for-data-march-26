# Control Flow ---> How does a program decide what to do next?

# Conditional Statements
age = 20

if age >= 18:
    print("You are officially an adult.")
    print("Unlucky!")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Comparison and logical operators
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed, enjoy the movie!")
else:
    print("Entry denied, age restricted or no ID")

# Using 'or'
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not'
light_on = False
if not light_on:
    print("Turn on the light!")

# Loops - Used to iterate over a sequence (e.g. a list, string, range)

# for loop
fruits = ["apples", "bananas", "pineapples"]
for fruit in fruits:
    print("I like", fruit)

# while loop
num = 1
while num <= 5:
    print(num)
    num += 1

# loops with a range
for i in range(10):
    print(i)