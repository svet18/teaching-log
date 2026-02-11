'''
Lesson Goals:
    - Use range() to generate a sequence of numbers, 
      control starting values, stopping points, and step size.
    - Practice iterating over ranges.
'''

print("\n\n")

# Create a range object 
#       - using range() function 
#       - with a stop argument only
# Verify that range() produces a range object
print(type(range(5)))


# Create a range object
#       - usinf range() function
#       - with start and stop arguments
# Use a for-loop
#   - to loop through a sequence of years
#   - and print the year each time the loop runs
for year in range(2020, 2026):
    print(year)

print("\n")


# Create a range object
#       - usinf range() function
#       - with start, stop, and step arguments
# Use a for-loop
#   - to loop through a sequence of years
#   - and print the year each time the loop runs
#     to verify that every other year is printed
for year in range(2020, 2026, 2):
    print(year)

print("\n\n")
