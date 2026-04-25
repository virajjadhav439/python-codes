import pandas as pd
import matplotlib.pyplot as plt
import re

class Student:
    def __init__(self, name, marks, email):
        self.name = name
        self.marks = marks
        self.email = email

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    def grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

class StudentSystem:
    def __init__(self):
        self.students = []

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def add_student(self):
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        email = input("Enter email: ")

        if not self.validate_email(email):
            print("Invalid email")
            return

        student = Student(name, marks, email)
        self.students.append(student)

    def save_to_csv(self):
        data = []
        for s in self.students:
            data.append([s.name, s.marks, s.result(), s.grade()])

        df = pd.DataFrame(data, columns=["Name", "Marks", "Result", "Grade"])
        df.to_csv("students.csv", index=False)

    def analyze(self):
        df = pd.read_csv("students.csv")
        print(df)

        print("\nAverage Marks:", df["Marks"].mean())
        print("Max Marks:", df["Marks"].max())
        print("Min Marks:", df["Marks"].min())

    def visualize(self):
        df = pd.read_csv("students.csv")
        plt.bar(df["Name"], df["Marks"])
        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.title("Student Performance")
        plt.show()

system = StudentSystem()

while True:
    print("\n1.Add Student\n2.Save\n3.Analyze\n4.Visualize\n5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.save_to_csv()
    elif choice == "3":
        system.analyze()
    elif choice == "4":
        system.visualize()
    elif choice == "5":
        break