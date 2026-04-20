def sum_of_digits_string(n):
    sum_o_digits = 0
    for i in n:
        sum_o_digits+=int(i)
    return sum_o_digits

n=num = input("Enter the number: ")
print(sum_of_digits_string(n))
