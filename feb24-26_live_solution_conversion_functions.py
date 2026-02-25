print("\n\n")
"""
Lesson Goals:
    - review and expand understanding of type conversion functions
    - understand how and why type conversion is used in real data-cleaning and validation tasks
    - practice using the list() function to converts iterable data (strings, ranges, tuples) into list objects
    - practice using the set() function to convert iterable data into sets and remove duplicates
    - understand the difference between the list() function and a list object
    - understand the difference between the set() function and a set object
    - compare lists vs sets and identify when each is appropriate in data processing
    """

# ---------------------------------
# Familiar conversion functions
# ---------------------------------
#   int()
#   float()
#   str()

var_list = ["age", "dependents", "gpa"]

# Create 3 separate variables from the list.
age, dependents, gpa = var_list

# Assign a value to each variable that would need to be converted.
# Create new converted variables.

age = "32"  # Here, age needs to be converted into an integer.
age_r = int(age)


dependents = 2  # Here, dependents needs to be converted into a string.
dependents_r = str(dependents)

gpa = "3.54"  # Here, gpa needs to be converted into a float.
gpa_r = float(gpa)

# Print type and value of all variables
# (original and converted)

print(type(age), age)
print(type(age_r), age_r)
print(type(dependents), dependents)
print(type(dependents_r), dependents_r)
print(type(gpa), gpa)
print(type(gpa_r), gpa_r)

# ---------------------------------
# New conversion functions - list(), set()
# ---------------------------------

# Create variables that hold:
#   - the word "noodle"
#   - rows as a tuple
#   - numbers from a range
# Verify each type & value

word = "noodle"
print(type(word), word)

rows = ("row1", "row2", "row3", "row4")
print(type(rows), rows)

numbers = range(5)
print(type(numbers), numbers)

# ---------------------------------
# Convert string => list => set => list
# ---------------------------------

# Convert the word "noodle" into a list & verify
letters = list(word)
print(type(letters), letters)

# Convert the list of letters in the word "noodle"
# to a set of unique letters only & verify
unique_letters = set(letters)
print(type(unique_letters), unique_letters)

# Convert the set of unique letters back to a list
list_unique = list(unique_letters)
print(type(list_unique), list_unique)

# ---------------------------------
# Convert tuple => set => list
# ---------------------------------

rows = ("row1", "row2", "row3", "row3")
print(type(rows), rows)

rows_set = sorted(set(rows))
print(type(rows_set), rows_set)

rows_unique_list = list(rows_set)
print(type(rows_unique_list), rows_unique_list)

# ---------------------------------
# Convert range => list
# ---------------------------------

# To retrieve the numbers from the range,
# convert the range to a list
numbers = list(range(5))
print(type(numbers), numbers)