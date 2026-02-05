
'''
Lesson goals:
    - Understand the use of nested if-statements 
    - Understand the important of proper indentation to preserve the hierarchy
    _ Use nested if-statements to evaluate conditions in a hierarchical order,
      checking primary requirements first and testing additional conditions
      if earlier criteria are met
'''
print()

student = True
us_resident = True
data_analytics = True
economics = True

# SCENARIO: Nested if-statements to evaluate multiple requirements

# Primary condition: Only students are eligible.
# Next condition: Only US residents are eligible.
# Next condition: Only data analytics economics majors are eligible.

if student:
    if us_resident:
        if data_analytics and economics:
            print("Eligible: Student meets residency and both program requirements.")
        else:
            print("Not eligible: Program requirements not fully met.")
    else:
        print("Not eligible: Student is not a U.S. resident.")
else:
    print("Not eligible: Applicant is not a student.")

print()
