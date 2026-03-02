# 20240802660
n = int(input("Enter the number of your choice : "))
Character = 97
# upper half
for i in range(n):
    # left dashes
    print("--" * (n - i-1), end="")

    # descending letters
    for j in range(i + 1):
        if  Character+n-j == Character+n and i==0:
            print(chr(Character + n - j - 1), end="")
        else:
            print(chr(Character + n - j - 1), end="-")

    # ascending letters
    for j in range(i - 1, -1, -1):
        if  Character+n-j == Character+n:
            print(chr(Character + n - j - 1), end="")
        else:
            print(chr(Character + n - j - 1), end="-")

    # right dashes
    print("--" * (n - i - 1))

# lower half
for i in range(n - 2, -1, -1):
    print("--" * (n - i - 1), end="")

    for j in range(i + 1):
        if  Character+n-j == Character+n and i==0:
            print(chr(Character + n - j - 1), end="")
        else:
            print(chr(Character + n - j - 1), end="-")


    for j in range(i - 1, -1, -1):
        if  Character+n-j == Character+n:
            print(chr(Character + n - j - 1), end="")
        else:
            print(chr(Character + n - j - 1), end="-")

    print("--" * (n - i - 1))
