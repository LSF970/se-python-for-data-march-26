# Lists - ordered, mutable collections of values. Allows duplicates

trainee_list = ["Abbas", "Luis", "Deepa", "Kojo"]
print(trainee_list)

# Indexing
print(trainee_list[0]) # print first element
print(trainee_list[-1]) # print last element --> useful because the list variable length
print(trainee_list[:3]) # print up to fourth index
print(trainee_list[2:]) # print from third index

# Check if specific value is in list
print("Deepa" in trainee_list) # Output is Bool (True or False)

# Change element of list
trainee_list[0] = "Bernadine"
print(trainee_list)

# Length of list
print(len(trainee_list))

# List methods
num_list = [1, 5, 6, 3, 75, 2]

# insert 450 at the second element of the list
num_list.insert(2, 450)
print(num_list)

# remove last element of list - if arguments left blank
num_list.pop()
print(num_list)

# remove the first element of a list
num_list.pop(0)
print(num_list)

# sort a list --> smallest to largest
num_list.sort()
print(num_list)

# Add element to the end of a list
num_list.append(45)
print(num_list)

# Slicing - Slice returns a portion of a list from Initial to End at a step size of IndexStep

# Syntax for slicing --> List[Initial : End : IndexStep]
my_list = [10, 20, 30, 40, 50, 60, 70]

# Show entire list
print(my_list[::])

# Start at 10, hit every step
print(my_list[-7::1])