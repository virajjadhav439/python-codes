# fenced matrix 
# 2024080252
m = int(input("Enter the Number of rows:"))
n = int(input("Enter the Number of cols:"))
print("\n")
matrix = []
for i in range(1,m+1):
    i_mat=[]
    if(i==1)or(i==(m)):
        for j in range(1,n+1):
            i_mat+=[1]
    else:
        for j in range(1,n+1):
            if (j==1) or (j==n):
                i_mat+=[1]
            else:
                i_mat+=[0]
    matrix.append(i_mat)
for k in matrix:
    print(k,"")
