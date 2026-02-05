'''
Lesson Goals:
    - Practice more the "not" operator

General logic:
    - 'not' flips the Boolean value.
    - When X is set to True, not X becomes False.
    - When X is set to False, not X becomes True.
    - The code inside the if-block will run only when that condition is True.
    - The other code will run if the "not" condition is False.
'''
print()

# ------------------------------------------
# EXAMPLE 1

adult = False

# When adult is True, not adult is False.
# When adult is False, not adult is True.

# Write the if-statement using: if not adult
# In the if-block, print the following.
# Use the .upper() function for emphasize NOT:
#   The "not" condition is True.
#   adult = value.
#   You are NOT an adult.

if not adult:
    # This would run if adult were False
    print('The "not" condition is True')
    print(f"adult = {adult}")
    print("You are " + "not".upper() + " an adult")
else:
    # This would run if adult were True
    print(f'The "not" condition is False')
    print(f"adult = {adult}")
    print("You are an adult")

print()
# ------------------------------------------
# EXAMPLE 2

logged_in = True

if not logged_in :
    # This would run if logged_in were False
    print(f'The "not" condition is True')
    print(f"logged_in = {logged_in}")
    print("You are NOT logged_in ")
else:
    # This would run if logged_in were True
    print(f'The "not" condition is False')
    print(f"logged_in = {logged_in}")
    print("You are logged_in ")

print()
# ------------------------------------------
# EXAMPLE 3

meet_prerequisite = True

if not meet_prerequisite:
    # This would run if meeting the prereq were False
    print(f'The "not" condition is True')
    print(f"meet_prerequisite = {meet_prerequisite}")
    print("You do NOT meet the prerequisite")
else:
    # This would run if meeting the prereq were True
    print(f'The "not" condition is True')
    print(f"meet_prerequisite = {meet_prerequisite}")
    print("You MEET the prerequisite")

print()
# ------------------------------------------