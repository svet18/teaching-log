'''
Lesson Goals:
    - Use different iterable types: string, lists
    - Practice iterating over these types
    - Check if an item exists within a list
    - Split the list
'''

print("\n\n")

# -------------------------------
# Loop through a STRING
# -------------------------------

# Example 1:
# Loop through each character/letter in a string (directly)
for letter in "Tuesday":
    print(letter)

print("\n")
# -------------------------------

# Example 2:
# Loop through each character/letter in a string (using a variable)
day = "Monday"
for letter in day:
    print(letter)

print("\n")

# -------------------------------
# Loop through a LIST
# -------------------------------

# From LAST TIME...Using the range() function

# Use the start and stop arguments of the range() function
# to loop through the range of years:
for year in range(2017, 2020):
    print(year)

print("\n")
# -------------------------------
# Pass the range of years from the range() function
# to a variable to hold that range
# Then use the variable in the loop:
years = range(2021, 2026)
for year in years:
    print(year)

print("\n")

# -------------------------------
# TODAY... Another SOLUTION - Using LIST[]:
# See the README_topics

# EXAMPLE 3:
#   - use the list of years/days directly in the loop code
for year in [22, 23, 24, 25]:
   print(year)
   
print("\n")
# -------------------------------
for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
    print(day)

print("\n")
# -------------------------------

# EXAMPLE 4:
#   - create a list of years/months
#   - pass the list to a variable
#   - use the variable in the loop code
years = [2000, 2010, 2020, 2030]
for year in years:
    print(year)

print("\n")
# -------------------------------
qrt = ["Jan", "Feb", "Mar", "Apr"]
for month in qrt:
    print(month)

print("\n")
# -------------------------------

# EXAMPLE 5:
#  - access values in a list and change them
years[0] = 1900
for year in years:
    print(year)

print("\n")

# -------------------------------
# EXAMPLE 6:
#  - check is a value in a list exists
if 2020 in years:
    print("Exists.")

print("\n")
# -------------------------------
# EXAMPLE 7:
#   - split the list
message = "We are learning how to split lists now"
words = message.split(" ")
print(words)