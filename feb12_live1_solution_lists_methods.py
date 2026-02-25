# Practice list
student_id = ["02", "03", "04", "05"]

# .append(value) = add a new item at the end
student_id.append("06")
print(student_id)

# .insert(index, value) = add a new item at the beginning
student_id.insert(0, "01")
print(student_id)

# .pop(index) = delete last item (06 is gone)
student_id.pop()
print(student_id)

# .pop(index) = delete first item (01 is gone)
student_id.pop(0)
print(student_id)

# .pop(index) = delete second item (03 is gone)
student_id.pop(1)
print(student_id)

# .count(value) = count # occurrences
#   => first add 01 (index 0) and 03 (index 2) back and duplicate 03
student_id.insert(0, "01")
student_id.insert(2, "03")
student_id.insert(2, "03")
print(f"ID Count: {student_id.count("03")}")

# .remove(value) = delete first occurrence only
student_id.remove("03")
print(student_id)

# .sort() = ascending
new_list = [12, 3, 7, 5]
new_list.sort()
print(new_list)

# .sort(everse=True) = descending
new_list.sort(reverse=True)
print(new_list)