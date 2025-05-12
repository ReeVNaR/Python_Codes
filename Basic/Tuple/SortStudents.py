# List of students as (name, marks)
students = [("Ranveer", 88), ("Pratiksha", 92), ("Aarav", 75), ("Sia", 85)]


sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Students sorted by marks (high to low):")
for name, marks in sorted_students:
    print(name, "->", marks)
