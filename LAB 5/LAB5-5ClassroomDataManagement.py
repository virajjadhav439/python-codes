Eng_marks = int(input("Enter English marks : "))
Math_marks = int(input("Enter Maths marks : "))
Sci_marks = int(input("Enter Science marks : "))
SS_marks = int(input("Enter SS marks : "))
Hindi_marks = int(input("Enter Hindi marks : "))

marks_list = [Eng_marks, Math_marks, Sci_marks, SS_marks, Hindi_marks]

subjects_tuple = ("English", "Maths", "Science", "SS", "Hindi")

marks_dict = {
    subjects_tuple[0]: marks_list[0],
    subjects_tuple[1]: marks_list[1],
    subjects_tuple[2]: marks_list[2],
    subjects_tuple[3]: marks_list[3],
    subjects_tuple[4]: marks_list[4]
}

marks_set = set(marks_list)

total = sum(marks_list)
average = total / len(marks_list)
highest = max(marks_set)
lowest = min(marks_set)

print("List:", marks_list)
print("Tuple:", subjects_tuple)
print("Dictionary:", marks_dict)
print("Set:", marks_set)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)