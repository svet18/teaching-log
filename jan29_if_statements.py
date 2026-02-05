"""
Lesson goal:
- Understand conditional logic (if-statements)
- Practice simple if-statements
- Practice multiple if-statements
- Understand proper indentation of if-statements
- Get familiar with ternary operators
- Use logical operators (and, or, not) in if-statements
- Practice chaining logical operators
- Practice all comparison operators in if-statements:
    > ;  >= ;  < ;  <= ;  == ;  !=
- Continue practice breaking code into multiple lines
"""

# LIVE-CODING starts here...

# --------------------------------------------------
# STEP 0.
# --------------------------------------------------
# Add a blank line in terminal for a better visual.
print()
# --------------------------------------------------
# STEP 1. -- Simple if-statements (if, no else)
# --------------------------------------------------
# Store today's temperature in a variable.
# Store the freezing temperature in another variable.

freezing_temperature = 32
today_temperature = 12

# SCENARIO:
# Check if today is BELOW freezing & print 2 statements how you feel about it
if today_temperature < freezing_temperature:
    print("It is below freezing today")
    print("I do not like it")

# --------------------------------------------------
# STEP 2 -- Simple if-statements (if...else)
# --------------------------------------------------
# SCENARIO:
# Check if today is 10 or more degrees BELOW freezing.
# Print a statement if this is so AND a different statement if it is NOT so
# For this solution, define a variable "message"
if freezing_temperature - today_temperature >= 10:
    message = "It is super cold today"
else:
    message = "It is not super cold today"
print(message)

# Refactor the above code using a ternary operator.
message = "It is VERY cold today" if freezing_temperature - today_temperature >= 10 else "It is not super cold today"
print(message)

# --------------------------------------------------
# STEP 3. -- Multiple if-statements (if ... elif ... else)
# --------------------------------------------------
# Add more conditions
# Practice using other comparison operators

# SCENARIO: 

# If today's temp is 10 or more degrees lower than the freezing temp
#   - msg to display: 
#       Today is xxx degrees Fahrenheit.
#       It is cold.
# However, if today's temp higher 
#   - msg to display: It is cold today, but not too bad.
# If neither of the above conditions is true
#   - msg to display: It is nice today
# NOTE: today's temperature cannot be higher than the freezing temp
today_temperature = 33
if today_temperature - freezing_temperature <= -10:
    print(f"Today is {today_temperature} degrees Fahrenheit.")
    print("It is VERY cold.")
elif today_temperature - freezing_temperature <= 0:
    print("It is cold today.")
else:
    print("It is nice today.")

# --------------------------------------------------
# STEP 4. -- Modeling more complex conditions with logical operators
# --------------------------------------------------

# Use 4 variables" student, us_resident, data_analytics, economics
student = True
data_analytics = True
economics = True

# SCENARIO: Practice "and" operator w/2 variables (if ... else)
if student and data_analytics:
    print("Both conditions are true.")
else:
    print("At least one condition is NOT true.")
    print("But we do not know which one")

# SCENARIO: Practice "or" operator w/2 variables (if ... else)
if student or data_analytics:
    print("At least one condition is true.")
else:
    print("Both conditions are NOT true.")

# SCENARIO: Practice "and/or" operators w/3 variables (if ... else)
# being a student is required; and being a data_analytics or economics are required
if student and (data_analytics or economics):
    print("Eligible")
else:
    print("Not eligible")

# SCENARIO: Practice "not" operator
student = True 
if not student:
    print("The condition 'Student = True' is reversed. Hence, you are not a student.")
else:
    print("The condition 'Student = True' is not reversed. Hence, you are a student.")

adult = False
if not adult:
    print("The condition 'Adult = False' is reversed to True. Hence, you are an adult.")
else:
    print("The condition 'Adult = False' is not reversed. Hence, you are not an adult.")
