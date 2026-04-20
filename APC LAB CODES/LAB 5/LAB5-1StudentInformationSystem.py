# Student Information System

studentDict = {}

name = input("Enter the name of student: ")
rollno = int(input("Enter the roll no of the student: "))
age = int(input("Enter the age of the student: "))
branch = input("Enter the branch of student: ")

studentDict["Name"] = name
studentDict["RollNo"] = rollno
studentDict["Age"] = age
studentDict["Branch"] = branch

for key in studentDict:
    print(key, ":", studentDict[key])