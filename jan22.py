"""
Lesson goal:
- Understand what a variable is, how it is created and used in basic functions
- Understand variable naming conventions
- Understand that Python is case-sensitive 
- Learn how to work with strings
- Practice creating variables for primitive data types (integers, floats, strings, Booleans)
- Practice calling variables inside the print() function
- Practice using formatted strings to dynamically generate text
"""

# print(22)  # age
# print(15 * 40)  # weekly earnings: $15/hour × 40 hours
# print(15 * 40 + 60)  # weekly income including a $60 side gig
# print((15 * 40 + 60) - 200)  # income after $200 weekly living expenses
# print((15 * 40 + 60) - 200 > 0)  # are you financially ok this week?
# print(This week’s total income: $660)
# print("This week’s expenses: $200")
# print("Income left after expenses: $460")

# 1. Store values in variables.
age = 22
weekly_earning = 15 * 40
total_weekly_income = weekly_earning + 60
weekly_expenses = 200
net_income = total_weekly_income - weekly_expenses
ok_financially = True

# 2. Print values, calling variables inside the print function.
print()
print(age)
print(weekly_earning)
print(total_weekly_income)
print(weekly_expenses)
print(net_income)
print(ok_financially)
print(f"This week’s total income: ${total_weekly_income}")
print(f"This week’s expenses: ${weekly_expenses}")
print(f"Income left after expenses: ${total_weekly_income - weekly_expenses}")
print()
