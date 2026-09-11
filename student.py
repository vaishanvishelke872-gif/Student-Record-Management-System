# Student Record Management System

students = []

def add_student(name, roll_no, course):
    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }
    students.append(student)

add_student("Vaishnavi", 1, "BCA")

print("Student Records:")
print(students)