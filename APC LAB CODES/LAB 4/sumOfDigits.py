# Sum of digits meaning 
# input : 555
# process: 5+5+5
# output : 15

# input:123456
# process : 1+2+3+4+5+6
# output : 21

#approch 1
def sum_of_digits_string(n):
    sum_o_digits = 0
    for i in n:
        sum_o_digits+=int(i)
    return sum_o_digits

n="555"
print(sum_of_digits_string(n))

#approach 2

def sum_of_digits_number(n):
    sum_o_digits=0
    while(n!=0):
        count=0 
        count+=1
        sum_o_digits+=(n - n//(10*count)*10)
        n=n//10
    return sum_o_digits

n=123456
print(sum_of_digits_number(n))

