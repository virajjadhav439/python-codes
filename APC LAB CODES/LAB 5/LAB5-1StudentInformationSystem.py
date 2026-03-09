# Student information System
studentDict= {}
name=input("enter the name of student:")
rollno=int(input("enter the roll no of the student :"))
age = int(input("Enter the Age of the student:"))
branch = input("enter the Branch of student:")

studentDict["Name"]=name
studentDict["RollNo"]=rollno
studentDict["Age"]=age
studentDict["Branch"]=branch

for i in studentDict:
    print(i," : ",studentDict[i])
