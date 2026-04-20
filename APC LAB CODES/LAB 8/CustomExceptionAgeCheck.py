
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("You are not eligible!")
    else:
        print("You are eligible.")

except ValueError:
    print("Invalid input! Please enter a valid number.")

except Exception as e:
    print("Error:", e)

finally:
    print("Program execution completed.")