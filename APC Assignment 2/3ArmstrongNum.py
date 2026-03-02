#20240802660
n = input("Enter A number to check Armstrong : ")
num_sum = 0
for i in n:
    num_sum += int(i)**3

if num_sum == int(n):
    print("True")
else:
    print("False")
