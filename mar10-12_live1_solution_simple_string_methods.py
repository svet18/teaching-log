"""
Lesson goals:
    - Name common data cleaning tasks.
    - Apply common string methods to standardize text data.
    - Use validation methods to verify data quality.
    - Transform text (names, emails, phone numbers) into clean, consistent formats.
"""
print("\n\n")

# Common Data Cleaning Issues/Tasks:
# -------------------------------------------------------
# 1. Blank cells or records (missing data)
# 2. Trailing spaces/punctuation
# 3. Inconsistent capitalization
# -------------------------------------------------------
# 4. Incorrect data types (e.g., numbers stored as text)
# 5. Duplicates
# 6. Extra spaces inside a string
# 7. Remove commas
# 8. Replace values
# -------------------------------------------------------
# 9. Replace looping through a list
# -------------------------------------------------------
# Missing or incomplete emails
# Unwanted leading characters (e.g., $)
# Inconsistent labels/category names
# Entries that should not have numeric characters
# All values must start with specific text (e.g., R0000)
# Names must end with specific text (e.g., _r)
# Unwanted newline characters
# Inconsistent separators

# -------------------------------------------------------
# 1. Blank cells or records (missing data)
names = [" John", " ", "", "Ann.", "mary"]
no_blanks = []

for name in names:
    if name.strip() != "":
        no_blanks.append(name)
print(no_blanks)


# -------------------------------------------------------
# 2. Trailing spaces/punctuation
no_trailing = []

for name in no_blanks:
    cleaned = name.lstrip(" ").rstrip(".")
    no_trailing.append(cleaned)
print(no_trailing)

# -------------------------------------------------------
# 3. Inconsistent capitalization
no_lowcase = []

for name in no_trailing:
    cleaned = name.capitalize()
    no_lowcase.append(cleaned)
print(no_lowcase)


# -------------------------------------------------------
# 1-3. Consolidated:
clean_names = []

for name in names:
    cleaned = name.strip()      # remove spaces both sides
    cleaned = cleaned.rstrip(".")  # remove trailing period
    cleaned = cleaned.capitalize()  # fix capitalization

    if cleaned != "":
        clean_names.append(cleaned)

print(clean_names)


# -------------------------------------------------------
# 4. Incorrect data types (e.g., numbers stored as text)
income_values = ["45000", "52000", "N/A", "61000", "45k"]

for value in income_values:

    # Check if the value contains only digits
    if value.isdigit():
        income = int(value)
        print("Valid income:", income)
    else:
        print("Invalid income value detected:", value)


# -------------------------------------------------------
# 5. Duplicates
text = "data science data analytics science python python"

# Step 1: Split the string into words
words = text.split()

# Step 2: Create an empty list for unique words
unique_words = []

# Step 3: Loop through words and add only if not already present
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Step 4: Join the list back into a string
clean_text = " ".join(unique_words)

print(clean_text)


# -------------------------------------------------------

# 6. Extra spaces inside a string
text_raw = "This   is   a    string   with   extra spaces"
clean_text = " ".join(text_raw.split())

print(clean_text)


# -------------------------------
# 7. Remove commas

text = "This, is, a, string, with, commas"
new_text = text.replace(",", "")
print(new_text, "\n")


# -------------------------------
# 8 Apply multiple replacements
text = "Data analytics is fun, fun, fun!"
new_text = text.replace(
    "fun", "powerful", 3
    )
print("Multiple replacements: ", new_text, "\n")


# -------------------------------
# 9. Replace looping through a list
income = "85,000 USD (estimated)"

to_remove = [",", "USD", "(",
    "estimated", ")"]

# take one item, replace it, update string, repeat
for item in to_remove:
    income = income.replace(item, "")

print("loop through list to replace: ", income.strip())


# -------------------------------
# Misc examples
# -------------------------------
# Detect missing or incomplete email addresses
emails = [
    "john.smith@company.com",
    "maryjanecompany.com",
    "   ",
    "alex@",
    "lisa.brown@gmail.com"
]
# Using multiple methods:
    # - .strip() => removes blank space entries
    # - email == "" => detects empty values
    # - "@" not in email => detects missing @
    # - .startswith("@") => detects missing username
    # - endswith("@") => detects missing domain

for email in emails:
    email = email.strip()

    if email == "" or "@" not in email or email.startswith("@") or email.endswith("@"):
        print(f"Invalid email detected: {email}")
    else:
        print(f"Valid email: {email}")

# Using .find()
    # - .strip() => removes blank space entries
    # - .find("@") => returns the index position of "@"
    # - .find() returns -1 if "@" is not found
    #       if at_position == 0 => email starts with "@" (missing username)
    #       if at_position == len(email) - 1 => email ends with "@" (missing domain)

for email in emails:
    email = email.strip()

    at_position = email.find("@")

    if email == "" or at_position == -1 or at_position == 0 or at_position == len(email) - 1:
        print(f"Invalid email detected: {email}")
    else:
        print(f"Valid email: {email}")

# ------------------------------
# Extract area code using slicing

phone = "(312) 555-7890"
area_code = phone[1:4]
print(area_code)

# ------------------------------
# Clean the names
names = ["  alice", "Bob ", "CHARLIE", "DaVid"]

clean_names = []
for name in names:
    cleaned = name.strip().title()
    clean_names.append(cleaned)
print(clean_names)

# Same code but using list comprehension
clean_names = [name.strip().title() for name in names]
print(clean_names)
