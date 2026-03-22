"""
Lesson goals:
    - Write UDFs - user-defined functions - that perform a task
    - Write UDFs that return a value
    - Write UDFs with and w/o parameters
    - Understand the difference bw. parameters and arguments
    - Store values returned by functions in variables

General Syntax:

def function_name():
    write code here that the function executes

UDFs can be categorized in two ways:

By what they do:
    1. Functions that perform a task
    2. Functions that return a value

By how they receive input:
    1. Functions without parameters
    2. Functions with parameters
"""

print("\n\n")



def get_info(gpa):
    print(gpa)

get_info(3.78)


""" Study these """
# ---------------------------------------
# Type 1.1: A user-defined function that 
#   - performs a task (prints a message)
#   - does not have a parameter; the message is hard-coded
#   - does not return a value

# Step 1. Define a function that prints a hard-coded exit message.
def exit_msg1():
    print("Action complete.")

# Step 2. Call the function.
exit_msg1()

# Step 3. Verify that it does not return a value.
print("Type 1.1: ", exit_msg1())

print("\n\n")


# ---------------------------------------
# Type 1.2: A user-defined function that
#   - performs a task (prints an exit message)
#   - receives input through a parameter
#   - does not return a value

# Step 1. Define a function with a parameter that would hold a message to print.
def exit_msg2(msg):
    print(msg)

# Step 2. Call the function and pass a message to the parameter.
exit_msg2("You are done.")

# Step 3. Verify that the function does not return a value.
print("Type 1.2: ", exit_msg2("You are done."))

print("\n\n")


# ---------------------------------------
# Type 2.1: User-defined function that
#   - does not have a parameter
#   - returns a value

# Step 1. Define a function that returns a message (hard-coded).
def exit_msg3():
   return "Ready to exit?"

# Step 2. Call the function and print the returned value.
print(exit_msg3())

# Step 3. Verify that the function returns a value.
print("Type 2.1: ", exit_msg3())

print("\n\n")


# ---------------------------------------
# Type 2.2: User-defined function that
#   - receives input through a parameter
#   - returns a value

# Step 1. Define a function with a parameter 
#         that would hold a message to print.
def exit_msg4(msg):
    return msg

# Step 2. Call the function, pass a message as an argument,
#         store the returned value in a variable & print.
message = exit_msg4("Good-bye.")
print(message)

# Step 3. Print the returned value to verify the function output.
print("Type 2.2: ", message)

print("\n\n")
