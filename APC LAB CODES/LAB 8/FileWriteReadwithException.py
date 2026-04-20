
# Writing to file
try:
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    file = open("students.txt", "a")
    file.write(f"Name: {name}, Marks: {marks}\n")
    file.close()

    print("Data written to file successfully.")

except ValueError:
    print("Invalid input! Marks should be a number.")

except Exception as e:
    print("Error while writing:", e)

# Reading from file
try:
    file = open("students.txt", "r")
    print("\nStudent Records:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error while reading:", e)

finally:
    print("\nProgram execution completed.")