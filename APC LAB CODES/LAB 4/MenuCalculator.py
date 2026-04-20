print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")

def calculate(x, y, choice):
    if choice == 1:
        add = lambda x, y: x + y
        return add(x, y)
    elif choice == 2:
        subtract = lambda x, y: x - y
        return subtract(x, y)
    elif choice == 3:
        multiply = lambda x, y: x * y
        return multiply(x, y)
    elif choice == 4:
        if y == 0:
            return "Cannot divide by zero"
        divide = lambda x, y: x / y
        return divide(x, y)
    else:
        return "Invalid choice"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = int(input("Enter your choice: "))

print("Result is:", calculate(num1, num2, choice))