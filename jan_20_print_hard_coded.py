"""
Lesson goal:
- Understand what an expression is
- Practice writing hard-coded expressions of different types
- Introduction to primitive data types:
    Integer
    Float 
    String (text)
    Boolean (True/False)
- Introduction to built-in functions: 
    print()
- Practice passing the value produced by an expression to the print function
  and printing it to the terminal

For each task:
    - use print() function
    - use hard-coded values inside the function
    - what you see in parentheses () is an expression
    - write a required expression, 
    - pass it to the print function & 
    - print the result to the terminal.
"""

# 1. Expression that evaluates to an integer.
print(13)

# 2. Expression that evaluates to a float.
print(2.7)

# 3. Expressions with arithmetic operations
print(2 + 2)
print(10 - 3)
print(3 * 11)
print(12/4)

# 4. Expressions to practice order precedence of arithmetic operations:
#   - parentheses first
#   - multiplication/division second
#   - addition/subrtaction third
print(2 + 2 * 3/2)
print(((2 + 2) * 3)/2)

# 5. Expressions that produce a letter F like shown.
# ********
# ********
# **
# **
# *****
# **
# **
# **
print("*" * 8)
print("*" * 8)
print("*" * 2)
print("*" * 2)
print("*" * 5)
print("*" * 2)
print("*" * 2)
print("*" * 2)

# 6. Boolean expression, comparing numbers.
print(2 > 3)
print(10 < 20)

# 7. Expression that evaluates to a string.
print("Today is Tuesday")

# 8. Expression that concatenates a string and a numeric value into a string.
print("Today is Tuesday, " + "January 20, ", 2026)
