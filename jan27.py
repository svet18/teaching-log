"""
Lesson goal:
- Understand the use of the input() function
- Store input in variables
- Convert text input into numbers using int() and float()
- Use .upper() method of the string object
- Practice using formatted strings (f-strings) to dynamically generate text
"""

# LIVE-CODING starts here...

# --------------------------------------------------
# Add a blank line in terminal for a better visual.
print()
# --------------------------------------------------
# STEP 1.
# Ask for a person's first name.
# HINT: use input().
# Do not store input in a variable.
input("What is your first name? ")

# STEP 2. 
# Store a person's first name input in a variable and print to the terminal.
first_name = input("What is your first name? ")
print(first_name)

# STEP 3. 
# Confirm that input() returns a string.
# HINT: use type()
print(type(first_name))

# --------------------------------------------------
# STEP 4. -- A more complete example 1.
#   Ask for an average regular gas price in Toledo today.
#   Store in a variable.
#   Print the value.
#   Verify that it is a string type using f-string: "Type : "
#   Convert to a float when creating a variable.
#   Verify conversion using f-string: "Type after conversion : "
#   Create a new variable to hold a converted value.
#   Verify conversion using f-string: "Type after conversion : "
#   Store city name in a variable.
#   Print a meaningful user-friendly summary:
#       The average regular gas price in TOLEDO on January 27, 2026: $2.50
#       HINT: use multiple f-strings, .upper() & formatting (fixed 2 decimals)
#   Print a blank line at the end

reg_gas_price = input("What is the regular gas price today in Toledo? ")  # get user input & store it in a variable
print(reg_gas_price)  # verify that it is stored
print(type(reg_gas_price))  # verify that the input function always returns a string
reg_gas_price = float(input("What is the regular gas price today in Toledo? "))  # convert it to a float, using the same variable
print(f"Type after conversion: {type(reg_gas_price)}")  # verify the conversion
converted_gas_price = float(reg_gas_price)  # alternatively, store a converted value in a new variable
print(converted_gas_price)
print(f"Type after conversion: {type(converted_gas_price)}")  # verify the type of the new variable
city = "Toledo"
print(
    f"The average regular gas price in {city.upper()} "
    f"on January 27, 2026: ${converted_gas_price:.2f}"
    )
print()
