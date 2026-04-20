# Approach 1
ls = [1, 4, 6, 7, 6, 8, 5, 10, 10]
set_ls = set(ls)
print(list(set_ls))

# Approach 2
unique_ls = []
for i in ls:
    if i not in unique_ls:
        unique_ls.append(i)

print(unique_ls)