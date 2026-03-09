# string vowels finding
# 20240802675
s = input("enter the string : ")
vowels_list =["a","A","e","E","i","I","o","O","u","U"]
vowels = "" 
consonants = ""
for ch in s:
    if ch in vowels_list:
        vowels = vowels+ch
    else:
        consonants = consonants + ch 
result = vowels + consonants 
print(result)     