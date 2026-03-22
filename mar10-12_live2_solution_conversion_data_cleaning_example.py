# Data-Cleaning Example:
# Survey data from employers about skills they want in new hires.
# Goal: have each row as a list of unique skills, nice and clean
print("\n\n")

raw_data = [
    "Excel, Python, SQL, Excel",
    "communication, teamwork, python",
    "Python,SQL , Communication ",
    "  Excel, Power BI, SQL, Excel  "
]
print("Raw data type: ", type(raw_data))
print(raw_data, "\n\n")

print("Each item in raw data: ", type(raw_data[0]))
print(raw_data[0], "\n\n")

# ---------------------------------------------
# Step 1. Convert each row to a list
# ---------------------------------------------
raw_rows = []

for row in raw_data:
    split_row = row.split(",")
    raw_rows.append(split_row)

print("Step 1 - RawRows type:: ", type(raw_rows))
print("Step 1: ", raw_rows)
print("\n")
print("Step 1: ", raw_rows[3])
print("\n")
print("Step 1: Each row in RawRows: ", type(raw_rows[3]))
print(raw_rows[0][0])

print("\n\n")

# ---------------------------------------------
# Step 2. Clean each row & create a list of cleaned rows:
#   - remove extra spaces
#   - capitalize
# ---------------------------------------------
cleaned_rows = []

for row in raw_rows:
    clean_row = []
    for skill in row:
        cleaned_skill = skill.strip().title()
    
        clean_row.append(cleaned_skill)
    cleaned_rows.append(clean_row)

print(cleaned_rows)
print("\n\n")

# ---------------------------------------------
# Step 3. Convert each row to a set of unique skills.
# ---------------------------------------------
unique_sets = []

for row in cleaned_rows:
    unique_sets.append(set(row))

print(unique_sets)

# ---------------------------------------------
# Step 4. Convert each row back to a list.
# ---------------------------------------------

final_rows= []

for row in unique_sets:
    final_rows.append(list(row))

print(final_rows)