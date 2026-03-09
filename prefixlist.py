l = ["racecar","dog","car"]

a = ""
for i in range(len(l)):
    temp = "" 
    j = i +1
    if j <len(l):
        for k in range(min(len(l[i]),len(l[j]))):
            if i == 0:
                while k<len(l[i]) and k<len(l[j]) and l[i][k] == l [j][k]:
                    temp = temp+l[i][k]
                    k=k+1
                a = a+temp
            else:
                while k<len(l[i]) and k<len(l[j]) and k<len(a) and l[i][k]==a[k]:
                    temp = temp+l[i][k]
                    k=k+1
                if len(a)>len(temp):
                    a = temp
print(a)

