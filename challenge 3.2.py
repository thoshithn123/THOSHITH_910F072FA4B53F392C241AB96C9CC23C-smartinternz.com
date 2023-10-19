class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Create a list of student objects
students = [
    Student("Alice", "A101", 3.8),
    Student("Bob", "B102", 3.5),
    Student("Charlie", "C103", 4.0),
    Student("David", "D104", 3.2),
]

# Call the sort_students function
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")