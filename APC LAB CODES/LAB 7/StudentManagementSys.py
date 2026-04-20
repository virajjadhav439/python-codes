
print("Welcome to Student Management System")

class Student:
    def __init__(self, name, prn, marks):
        self.name = name
        self.prn = prn
        self.marks = marks

    def grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 50:
            return 'C'
        else:
            return 'F'

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.prn)
        print("Marks:", self.marks)
        print("Grade:", self.grade())


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter name: ")
        roll_no = int(input("Enter roll number: "))
        marks = list(map(int, input("Enter marks (space separated): ").split()))

        student = Student(name, roll_no, marks)
        self.students.append(student)
        print("Student added successfully!\n")

    def display_students(self):
        if not self.students:
            print("No student records found.")
        else:
            for student in self.students:
                print("\nStudent Details:")
                student.display()


# Main Program
sms = StudentManagementSystem()

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        sms.add_student()
    elif choice == '2':
        sms.display_students()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")