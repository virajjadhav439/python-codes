n=int(input("Enter a Number To Create Pascals Triangle : "))
def print_Row(row_matrix):
    for i in row_matrix:
        print(i,end=" ")
Row_matrix = [1]
variable_matrix =[1]
# spaces

for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(len(Row_matrix)-1):
        variable_matrix[j+1] = Row_matrix[j]+Row_matrix[j+1]
    Row_matrix = variable_matrix[:]
    variable_matrix+=[1]
    print_Row(Row_matrix)
    print()