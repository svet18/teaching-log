# -------------------------------------------------
# While-loop examples
# -------------------------------------------------

# While-Loop Applied Buckets:

# 1) until we reach ... 
#       - Keep accepting surveys until we collect 100 surveys
#       - Keep enrolling teachers Until 15 PD seats are filled
# 2) until no more ...
#       - Remove blank rows until none remain
#       - Remove duplicate IDs until none remain
#       - Remove invalid survey responses until none remain
# 3) until found ...
#       - Find first missing value in a column
#         and stop as soon as the item is found
# 4) until cleaned ...
#       - Keep fixing phone numbers until length = 10
#       - Keep removing rows with missing key variables until clean
#       - Replace blanks with averages until dataset has no missing value
#       - Remove extra spaces in a name
#       - Strip symbols from phone numbers
#       - Fix capitalization of emails
#  5) until user stops ...
#  6) until target is met ...
#       - Keep sending emails until we raise $3000

# -------------------------------------------------
# 1) until we reach ... 
# -------------------------------------------------
print("Example 1: until we reach ...")
# A program has 30 seats. Students are ranked by score.
# Admissions keeps accepting students until seats are full.
# You have 3 seats remaining
ranked_scores = [98, 96, 95, 93, 92, 91, 90, 89, 88, 87]
seats = 3

accepted = []
i = 0

while len(accepted) < seats:
    accepted.append(ranked_scores[i])
    i += 1

print("\n Accepted students's scores: ", accepted, "\n")

# -------------------------------------------------
# 2) until no more ...
# -------------------------------------------------
print("Example 2: until no more ...")
# Remove duplicate rows
rows = [
    "LP001,Male,Graduate,Y",
    "LP002,Female,Graduate,N",
    "LP001,Male,Graduate,Y",
    "LP003,Male,Not Graduate,Y",
    "LP002,Female,Graduate,N"
]

clean_rows = []
duplicate_count = 0
i = 0

while i < len(rows):
    if rows[i] not in clean_rows:
        clean_rows.append(rows[i])
    else:
        duplicate_count += 1
    i += 1

print("Clean dataset:")
for row in clean_rows:
    print(row)

print("\nDuplicates removed:", duplicate_count)

# -------------------------------------------------
# 3) until found ...
# -------------------------------------------------
print("Example 3: until found ...")
# You work in fraud analytics.
# Transactions above $5,000 must be reviewed manually.
# You need to scan transactions until the first suspicious one is found, then stop.

transactions = [120, 85, 230, 450, 980, 1200, 7200, 300, 150]

i = 0

while transactions[i] <= 5000:
    i += 1

# To insert emoji: Start + "." (pc); Ctrl + Cmd + Space (mac)
print("⚠️ Suspicious transaction found:")
print("Amount:", transactions[i])
print("Position in dataset:", i)

# -------------------------------------------------
# 4) until cleaned...
# -------------------------------------------------

# Remove double spaces
print("Example 4a: until cleaned ...")

name = "John   Smith"

while "  " in name:
    name = name.replace("  ", " ")
print(name)


# Clean phone number
print("Example 4b: until cleaned ...")
phone = "(419) 555-1234"

while not phone.isdigit():
    #phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    phone = (
        phone.replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )

print(phone)

# Remove duplicates
print("Example 4c: until cleaned ...")
customers = ["A","B","A","C","B","D"]

# (optional) count duplicates BEFORE cleaning
duplicates_removed = len(customers) - len(set(customers))

# remove duplicates
while len(customers) != len(set(customers)):
    customers = list(set(customers))

print("Clean customers:", customers)
print("Duplicates removed:", duplicates_removed)

# -------------------------------------------------
# # 5) until user stops ...
# -------------------------------------------------
print("Example 5: until user stops ...")

scores = []
entry = ""

while entry != "done":
    entry = input("Enter score or type done: ")
    if entry != "done":
        scores.append(int(entry))

print(scores)

# -------------------------------------------------
# 6) until target is met
# -------------------------------------------------
print("Example 6: until target is met ...")
donations = [5000, 12000, 8000, 15000, 9000]
goal = 40000
total = 0
i = 0

while total < goal:
    total += donations[i]
    i += 1

print("Goal reached:", total)
