'''
Lesson Goals:
    - Different ways of defining tuples
    - Practice checking for items stored in tuples
'''

print("\n\n")

# Tuples represent a single record that does not change

# Store student record in a tuple:
#   - gender
#   - age
#   - enrollment status (full-time or part-time)
#   - gpa
#   - next semester enrollment (Yes/No)

# 3 different ways of defining a tuple:
#   ()
#   no ()
#   concatenating tuples

student = ("Male", 22, "Full-time", 3.7, "Yes")
print("1: ", student)
student = "Male", 22, "Full-time", 3.7, "Yes"
print("2: ", student)
student = ("Male", 22,) + ("Full-time", 3.7, "Yes")
print("3: ", student)

if "Male" in student:
    print("Exists.")

print("\n")