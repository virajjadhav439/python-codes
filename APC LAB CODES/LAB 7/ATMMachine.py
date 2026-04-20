
print("Welcome to ATM Simulation System")

def menu():
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("\nCurrent Balance:", self.balance)

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("Invalid deposit amount\n")
        else:
            self.balance += deposit_amount
            print("Amount Deposited Successfully")
            print("Updated Balance:", self.balance, "\n")

    def withdraw(self, withdrawn_amount):
        if withdrawn_amount <= 0:
            print("Invalid withdrawal amount\n")
        elif withdrawn_amount > self.balance:
            print("Insufficient balance\n")
        else:
            self.balance -= withdrawn_amount   # FIXED (you had = instead of -=)
            print("Please collect your cash")
            print("Updated Balance:", self.balance, "\n")


# Create user
user = ATM(1234, 0)

# PIN verification
attempts = 3
while attempts > 0:
    pin = int(input("\nEnter Your Pin: "))
    if pin == user.pin:
        print("PIN verified successfully")
        menu()
        break
    else:
        attempts -= 1
        print("Incorrect PIN. Attempts left:", attempts)

if attempts == 0:
    print("Card blocked. Too many incorrect attempts")
    exit()

# Main loop
while True:
    choice = input("\nEnter the function number you want to perform: ")

    if choice == "1":
        user.check_balance()

    elif choice == "2":
        user.deposit(int(input("Enter amount to deposit: ")))

    elif choice == "3":
        if user.balance == 0:
            print("No balance available. Please deposit money first\n")
        else:
            user.withdraw(int(input("Enter amount to withdraw: ")))

    elif choice == "4":
        print("Thank you for using the ATM!")
        print("Have a nice day")
        break

    else:
        print("Invalid choice! Please try again\n")