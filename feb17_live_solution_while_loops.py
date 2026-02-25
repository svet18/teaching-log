
print("\n\n")
"""
Lesson Goals (understand and practice):
    - count-controlled loops and condition-controlled loops
    - when to use:
        for loop with range()
        for loop with a fixed collection (tuple)
        while loop with a counter
        while loop with a sentinel value

    - how the break statement stops a loop early
    - how the else clause on loops works and when it runs
"""
# -------------------------------------------------
# For-loop example from feb 10 - 3 user attempts 
# using range()
# -------------------------------------------------

# 1. Using range()
print("Using range()")
attempts = range(1, 4)

for attempt in attempts:
    student_status = input("Student (Y/N): ").upper()

    if student_status == "Y" or student_status == "N":
        print("Entry accepted.")
        break
    else:
        print("Invalid entry. Attempt", attempt + 1)
else:
    print("3 failed attempts.")

print("\n\n")

# -------------------------------------------------
# For-loop example from feb 10 - 3 user attempts 
# using a tuple, since # attempts is fixed
# -------------------------------------------------

print("Using tuple")

# Define the tuple - can use () or not
attempts = 1, 2, 3

# Verify that it is a tuple
print(type(attempts))

# The code is exactly the same as above
for attempt in attempts:
    student_status = input("Student (Y/N): ").upper()

    if student_status == "Y" or student_status == "N":
        print("Entry accepted.")
        break
    else:
        print("Invalid entry. Attempt", attempt + 1)
else:
    print("3 failed attempts.")

print("\n\n")

# -------------------------------------------------
# The same scenario - 3 user attempts
# using a while-loop
# -------------------------------------------------
print("Using while loop")

# Step 1. Start the counter variable
attempt = 0

# Step 2. Run the code until attempt < 3:
# The code inside the loop is identical to the for-loop code
# except when we update the counter variable

while attempt < 3:

    student_status = input("Student (Y/N): ").upper()

    if student_status == "Y" or student_status == "N":
        print("Entry accepted.")
        break
    else:
        print("Invalid entry. Attempt", attempt + 1)

        # Update the counter variable!!!
        attempt += 1
else:
    print("3 failed attempts.")

print("\n\n")

# -------------------------------------------------
# While-loop example using a sentinel-controlled loop (w/STOP sign)
# -------------------------------------------------

# Scenario:
# Display a prompt until the user answers "Yes"

answer = ""

while answer != "Yes":
    answer = input("Type "Yes" to continue...")
print("Thank you")

# -------------------------------------------------
# More while-loop examples - next time...
# -------------------------------------------------

# While-Loop Applied Buckets:

# 1) until we reach ... 
#       - Keep accepting surveys until we collect 100 surveys
#       - Keep enrolling teachers Until 15 PD seats are filled
# 2) until no more ...
#       - Remove blank rows until none remain
#       - Remove duplicate IDs until none remain
#       - Remove invalid survey responses until none remain
# 3) until found ...
#       - Find first missing value in a column
#         and stop as soon as the item is found
# 4) until cleaned ...
#       - Keep fixing phone numbers until length = 10
#       - Keep removing rows with missing key variables until clean
#       - Replace blanks with averages until dataset has no missing value
#       - Remove extra spaces in a name
#       - Strip symbols from phone numbers
#       - Fix capitalization of emails
#  5) until user stops ...
#  6) until target is met ...
#       - Keep sending emails until we raise $3000
# -------------------------------------------------