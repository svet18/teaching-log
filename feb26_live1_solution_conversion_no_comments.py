print("\n\n")

# var_list = ["age", "dependents", "gpa"]
var_list = ["32", "2", "3.54"]

age, dependents, gpa = var_list

age = var_list[0]
age_r = int(age)

dependents = var_list[1]
dependents_r = str(dependents)

gpa = var_list[2]
gpa_r = float(gpa)

print(type(age), age)
print(type(age_r), age_r)
print(type(dependents), dependents)
print(type(dependents_r), dependents_r)
print(type(gpa), gpa)
print(type(gpa_r), gpa_r)

# ---------------------------------
# New conversion functions - list(), set()
# ---------------------------------

word = "noodle"
print(type(word), word)

rows = ("row1", "row2", "row3", "row4")
print(type(rows), rows)

numbers = range(5)
print(type(numbers), numbers)

# ---------------------------------
# Convert string => list => set => list
# ---------------------------------

letters = list(word)
print(type(letters), letters)

unique_letters = set(letters)
print(type(unique_letters), unique_letters)

list_unique = list(unique_letters)
print(type(list_unique), list_unique)

# ---------------------------------
# Convert tuple => set => list
# ---------------------------------

rows = ("row1", "row2", "row3", "row3")
print(type(rows), rows)

rows_set = sorted(set(rows))
print(type(rows_set), rows_set)

rows_unique_list = list(rows_set)
print(type(rows_unique_list), rows_unique_list)

# ---------------------------------
# Convert range => list
# ---------------------------------

numbers = list(range(5))
print(type(numbers), numbers)
