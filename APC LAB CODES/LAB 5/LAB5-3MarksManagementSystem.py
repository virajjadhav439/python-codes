
Eng_marks = int(input("Enter English marks: "))
Math_marks = int(input("Enter Maths marks: "))
Sci_marks = int(input("Enter Science marks: "))
SS_marks = int(input("Enter SS marks: "))
Hindi_marks = int(input("Enter Hindi marks: "))

marks = [Eng_marks, Math_marks, Sci_marks, SS_marks, Hindi_marks]

print("Maximum Marks:", max(marks))
print("Minimum Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))