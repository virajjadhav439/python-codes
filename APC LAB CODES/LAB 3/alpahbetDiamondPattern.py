# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

n = 5

# upper half
for i in range(n):
    # left dashes
    print("--" * (n - i-1), end="")

    # descending letters
    for j in range(i + 1):
        if  97+n-j == 97+n and i==0:
            print(chr(97 + n - j - 1), end="")
        else:
            print(chr(97 + n - j - 1), end="-")

    # ascending letters
    for j in range(i - 1, -1, -1):
        if  97+n-j == 97+n:
            print(chr(97 + n - j - 1), end="")
        else:
            print(chr(97 + n - j - 1), end="-")

    # right dashes
    print("--" * (n - i - 1))

# lower half
for i in range(n - 2, -1, -1):
    print("--" * (n - i - 1), end="")

    for j in range(i + 1):
        if  97+n-j == 97+n and i==0:
            print(chr(97 + n - j - 1), end="")
        else:
            print(chr(97 + n - j - 1), end="-")


    for j in range(i - 1, -1, -1):
        if  97+n-j == 97+n:
            print(chr(97 + n - j - 1), end="")
        else:
            print(chr(97 + n - j - 1), end="-")

    print("--" * (n - i - 1))
