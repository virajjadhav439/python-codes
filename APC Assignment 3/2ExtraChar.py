def find_extra_char(s1, s2):
    result = 0

    for ch in s1:
        result ^= ord(ch)

    for ch in s2:
        result ^= ord(ch)

    return chr(result)


# Example
s1 = "abcd"
s2 = "cedab"

print(find_extra_char(s1, s2))