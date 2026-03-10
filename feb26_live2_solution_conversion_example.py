# ---------------------------------
# Simple Data Cleaning Example
# ---------------------------------

raw_data = [
    "Excel, Python, SQL, Excel",
    "Python, SQL, Excel, Python",
    "Python, Power BI, SQL, Excel, Power BI"
]

clean_rows = []

for row in raw_data:
    split_row = row.split(", ")
    skill_set = set(split_row)
    clean_rows.append(skill_set)

print("\n", clean_rows[0], "\n")
print("\n", clean_rows[1], "\n")
print("\n", clean_rows[2], "\n")