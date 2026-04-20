n = int(input("Enter a Number To Create Pascal's Triangle: "))

row = [1]

for i in range(n):
    # spacing for pyramid shape
    print(" " * (n - i), end="")
    
    # print row
    for num in row:
        print(num, end=" ")
    print()
    
    # generate next row
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)
    
    row = next_row