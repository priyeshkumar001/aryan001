# Student dictionary
students = {
    101: {"name": "Rahul", "course": "BCA", "marks": 85},
    102: {"name": "Anita", "course": "BBA", "marks": 90},
    103: {"name": "Aman", "course": "BCA", "marks": 78},
}

# Display all students
print("Student Records:")
for roll, info in students.items():
    print("Roll No:", roll)
    print("Name:", info["name"])
    print("Course:", info["course"])
    print("Marks:", info["marks"])
    print()

# Add new student
students[104] = {"name": "Riya", "course": "BCA", "marks": 88}

# Update marks
students[101]["marks"] = 92

# Delete a student
del students[103]

print("Updated Student Records:")
print(students)
