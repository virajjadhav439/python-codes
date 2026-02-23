# lower half
for i in range(n - 2, -1, -1):
    print("--" * (n - i - 1), end="")

    for j in range(i + 1):
        print(chr(65 + n - j - 1), end="-")

    for j in range(i - 1, -1, -1):
        print(chr(65 + n - j - 1), end="-")

    print("--" * (n - i - 1))
