# Student Marks Analysis Project

# Step 1: Data (students and their marks)
students = {
    "Rahul": 85,
    "Balaji": 90,
    "Anjali": 78,
    "Kiran": 88,
    "Sneha": 92
}

# Step 2: Calculate average marks
total = sum(students.values())
average = total / len(students)

# Step 3: Find top student
top_student = max(students, key=students.get)

# Step 4: Display results
print("Student Marks Analysis")
print("----------------------")
print("Average Marks:", average)
print("Top Student:", top_student)
print("Top Marks:", students[top_student])
