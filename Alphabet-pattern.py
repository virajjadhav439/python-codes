n = 5

# upper half
for i in range(n):
    # left dashes
    print("--" * (n - i-1), end="")

    # descending letters
    for j in range(i + 1):
        if  65+n-j == 65+n and i==0:
            print(chr(65 + n - j - 1), end="")
        else:
            print(chr(65 + n - j - 1), end="-")

    # ascending letters
    for j in range(i - 1, -1, -1):
        if  65+n-j == 65+n:
            print(chr(65 + n - j - 1), end="")
        else:
            print(chr(65 + n - j - 1), end="-")

    # right dashes
    print("--" * (n - i - 1))

# lower half
for i in range(n - 2, -1, -1):
    print("--" * (n - i - 1), end="")

    for j in range(i + 1):
        if  65+n-j == 65+n and i==0:
            print(chr(65 + n - j - 1), end="")
        else:
            print(chr(65 + n - j - 1), end="-")


    for j in range(i - 1, -1, -1):
        if  65+n-j == 65+n:
            print(chr(65 + n - j - 1), end="")
        else:
            print(chr(65 + n - j - 1), end="-")

    print("--" * (n - i - 1))
