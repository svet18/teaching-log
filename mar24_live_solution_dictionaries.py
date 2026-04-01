"""
Lesson Goals:
    - Understand how dictionaries store data as key-value pairs
    - Create dictionaries using different data types (strings, integers, lists)
    - Access dictionary values using keys
    - Recognize that keys are not limited to strings
    - Retrieve values using .get() method
    - Add new key-value pairs to a dictionary
    - Update existing values individually and in bulk using .update()
    - Remove items using del and .pop() and understand their differences
    - Capture and reuse values removed from dictionaries
    - Determine dictionary size using len()
    - Explore dictionary structure using .keys(), .values(), and .items()
    - Iterate through dictionaries using loops (keys only vs. key-value pairs)
    - Check for the existence of keys and values using in
"""
# --------------------------------------------------------------------
"""
Quick reference:

List = mutable, ordered collection
Tuple = immutable, ordered collection
Set = mutable collection of unique, unordered values
Dictionary = mutable collection of key–value pairs (keys are unique)

List = [...]
Tuple = (...)
Set = {...}
Dictionary = {"key" : "value"}
"""
# --------------------------------------------------------------------


# Store a student record in a dictionary 
student = {
    'name': 'John',
    'age': 25,
    'courses': ['DA2', 'Stats1']
}

# Verify: {'name': 'John', 'age': 25, 'courses': ['DA2', 'Stats1']}
print(student)


# ----------
# Access any value from the dictionary using key
print("\n", student['name'])


# ----------
# Keys are not limited to strings
# E.g., Store rating scale values in a dictionary
scale = {
    1 : "Disagree",
    2 : "Neither disagree nor agree",
    3 : "Agree"
}

# Access any value from the dictionary using key
print("\n", scale[1])


# ----------
# Handle keys that do not exist to avoid a KeyError
# print(scale[4])   # throws a KeyError
print("\n", scale.get(4)) # returns a default value 'None' if a value does not exist
print("\n", scale.get(4, 'Not found'))    # returns a custom value 'Not found' of a value does not exist


# ----------
# Add values to a dictionary
scale[4] = "Strongly agree"

print("\n", scale.get(4))
print("\n", scale)


# ----------
# Update individual values in a dictionary
scale[1] = "Disagree"
scale[2] = "Somewhat disagree"
scale[3] = "Somewhat agree"
scale[4] = "Agree"

print("\n", scale, "\n")


# ----------
# Update multiple values in dictionary using .update() method
# Update the scale first. Then print the updated object.
scale.update({1: 'Strongly Disagree', 2: 'Disagree', 3: 'Agree', 4: 'Strongly agree'})

print("\n", scale, "\n")


# ----------
# Delete dictionary pairs:
del scale[4]

print("\n", scale, "\n")


# ----------
# Delete a dictionary pair, using .pop method
# and store a deleted value in a variable
courses = student.pop("courses")

print("\n", student, "\n")
print(courses)


# ----------
# Get dictionary information:
#   - size, using len()
#   - keys, using .keys()
#   - values, using .values()
#   - key-value pairs, using .items()
print("\n", len(scale), "\n")       # returns the number of key-value pairs
print("\n", student.keys(), "\n")   # returns a list of keys
print("\n", scale.values(), "\n")   # returns a list of values
print("\n", scale.items(), "\n")    # returns a list of tuple pairs


# ----------
# Loop through keys in a dictionary
for key in scale:
    print(key)


# ----------
# Loop through keys & values in a dictionary, using .items()
for key, value in scale.items():
    print(key, value)


# ----------
# Look up if a dictionary key exists
print(1 in scale)

# Look up if a dictionary value exists, using .values()
# print("Agree" in scale.values())
print("Agree" in scale)


# ----------
# Use dictionary as Counter
# This is similar to running frequencies on any
# categorical variable in some dataset
# where you do not need to know the categories in advance

# E.g., after you split data into rows and columns
# and can access column values as a list,
# you can loop through those, count each category and 
# store those as (cat.name : cat. frequency) pair in a dictionary
loan_status = ["Y", "N", "Y", "Y", "Y", "N"]

# This is the end result:
loan_status_dict = {
    "Y" : 4,
    "N" : 2
}

cat_counts = {} # create an empty dictionary

# A solution, using if-statement method
for cat in loan_status:
    if cat not in cat_counts:
        cat_counts[cat]=0
    cat_counts[cat]+=1

print(cat_counts)

# A shorter solution, using .get() method
cat_counts = {} # reset the dictionary

for cat in loan_status:
    cat_counts[cat] = cat_counts.get(cat, 0) + 1    # if cat is not in the dictionary, return 0

print(cat_counts)


# ----------
# Nested dictionary (like rows in a dataset)
employees = {
    1: {"name": "John", "dept": "Sales"},
    2: {"name": "Ana", "dept": "HR"}
}

# Access values in a nested dictionary using 2 keys
print(employees[1]["name"])


# ----------
# Clear a dictionary, using .clear() method
employees.clear()   # empties dictionary
print(employees)


# ---------------------------
# Using UDfs and dictionaries
# ---------------------------

# Task: Store category freqiencies in a dictionary

# Write a function to count category fequencies
# Make sure it returns the counts
# In this function, the key is the category (e.g., Y or N) 
# and the value is the frequency of that category
def count_values(data_list):
    counts = {}
    
    for value in data_list:
        counts[value] = counts.get(value, 0) + 1 # take the current count, or 0 if it’s new, & update it by adding 1
    
    return counts   # save the updated count

# Supply the data list
status = ["Y", "N", "Y", "Y"]

# Print counts of values in the data list
print(count_values(status))

# ----------
# Task: Store averages in a dictionary

def compute_average(data_dict, column):
    values = data_dict[column]
    return sum(values) / len(values)

data_dict = {
    'Gender' : ['Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
    'Married' : ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
    'Income': [6000, 5417, 2333, 3036, 4006, 12841],
    'Co-income': [0, 4196, 1516, 2504, 1526, 10968]
}

print(compute_average(data_dict, "Co-income"))


# ---------------------------
# have some FUN!
# ---------------------------

# Build your own emoji dictionary
emoji_dict = {}

# Add key-value pairs
emoji_dict["happy"] = "😊"
emoji_dict["sad"] = "😢"
emoji_dict["love"] = "❤️"
emoji_dict["fire"] = "🔥"
emoji_dict["thumbs_up"] = "👍"

# Print the whole dictionary
print(emoji_dict)

# Look up one emoji
print(emoji_dict["happy"])

# Add a new emoji later
emoji_dict["star"] = "⭐"

# Update an emoji
emoji_dict["sad"] = "☹️"

# Print updated dictionary
print(emoji_dict)