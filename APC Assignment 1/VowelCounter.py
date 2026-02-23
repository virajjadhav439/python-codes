# string vowels finding
# 20240802652
s = input("enter the string : ")
vowels_list =["a","A","e","E","i","I","o","O","u","U"]
vowels = 0
for ch in s:
    if ch in vowels_list:
        vowels+=1
result = vowels
print("The Number of Vowels in the word:",s,"is",result)     