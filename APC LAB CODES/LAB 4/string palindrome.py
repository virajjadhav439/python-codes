def palindrome():
    string = input("Enter the string: ")
    rev = ""

    for i in range(len(string) - 1, -1, -1):
        rev += string[i]

    if string == rev:
        print(string, "is palindrome")
    else:
        print(string, "is not palindrome")

palindrome()