"""
Practice applying conditional logic inside a for-loop to:
    - repeat user input prompt and enforce simple validation rules and
    - accept valid input,
    - reject invalid input,
    - stop execution early using break
Use the condition logic in the for-loop to:
    - calculate frequencies
"""
# -------------------------------
print("\n\n")

# SCENARIO 1 - Validate input w/3 attempts

# We want to ask if the user is a student
# We prompt the user to enter Y or N 
# We convert the user response to an upper case Y or N
# We want to give the user up to 3 attempts
# For each attempt...
#   If the user enters Y or N:
#       - We want to let the user know that their entry was accepted
#       - and stop the other attempts from running
#       (i.e., we want to get out of the loop)
#   If the entry is invalid:
#       - We want to let the user know and display attempt #
#   If the user does not enter Y or N and uses all 3 attempts:
#       - We tell the user that they had 3 failed attempts
#       - and exit the loop

for attempt in range(1, 4):
    student = input("Student (Y/N): ").upper()

    # Validate input
    if student == "Y" or student == "N":
        print("Entry accepted.")
        break
    else:
        print("Invalid entry. Attempt", attempt)
else:
    print("3 failed attempts.")

print("\n\n")

# -------------------------------
# SCENARIO 2 - Calculate frequencies

# We have a list of students and their attendance data
# We want to count students in attendance and report it out

attendance = ["Y", "N", "Y", "Y", "N"]
attendance_count = 0
for status in attendance:
    if status == "Y":
        attendance_count += 1

print("# Students in Attendance:", attendance_count)

print("\n\n")