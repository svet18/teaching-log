'''
Lesson Goals:
    - Understand how chained comparison operators work in Python and 
      how they differ from using multiple logical conditions
      - Use chained operators to implement realistic rules 
       (eligibility, thresholds, and classifications) in simple decision-making
'''

print()

# ------------------------------------------
# EXAMPLE 1

income = 42000

# If income is at least $30K but less than $60K 
# ==> Eligible for mid-income assistance program

# SOLUTION 1: Using multiple logical operators
# Print message at the end
if income >=30000 and income < 60000:
    message = "Eligible for mid-income assistance program"
else:
    message = "Ineligible for mid-income assistance program"
print(message)


# SOLUTION 2: Using chaining operators
# Print message within each block
if 30000 <= income < 60000:
    print("Eligible for mid-income assistance program")
else:
    print("Ineligible for mid-income assistance program")

# ------------------------------------------
# EXAMPLE 2

credit_score = 685

# If credit score is at least 650 but less than 720 
# ==> Moderate credit risk
# If less than 650 ==> High credit risk
# If 720 or higher ==> Low credit risk

# SOLUTION 1: Using multiple logical operators
if credit_score >= 650 and credit_score < 720:
    print("Moderate credit risk")
elif credit_score < 650:
    print("High credit risk")
else:
    print("Low credit risk")


# SOLUTION 2: Using chaining operators
if 650 <= credit_score < 720:
    print("Moderate credit risk")
elif credit_score < 650:
    print("High credit risk")
else:
    print("Low credit risk")