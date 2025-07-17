students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]

# Calculate percentage and add to dictionary
for student in students:
    total = sum(student["marks"])
    percentage = total / 3  # Assuming 3 subjects, each out of 100
    student["per"] = round(percentage, 2)

# Sort by percentage in descending order
students_sorted = sorted(students, key=lambda x: x["per"], reverse=True)

# Print using .format()
index = 1
for student in students_sorted:
    print("{}. {} stands {}: {}%".format(index, student["name"], index, student["per"]))
    index += 1
