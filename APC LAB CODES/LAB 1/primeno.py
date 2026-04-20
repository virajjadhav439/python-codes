# prime number
# Name : Viraj Jadhav
# 20240802660
num = int(input("emter number : "))
count = 0 
for i in range (1,num+1):
    if num % i == 0:
        count = count+1 
if count == 2:
    print ("prime number ")
else:
    print ("not a prime number ") 