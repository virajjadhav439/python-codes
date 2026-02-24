ls =eval(input("enter the list "))

is_prime = lambda n: (
    False if n <= 1 else 
    check_prime(n)
)

def check_prime(n):
    for i in range(2,n):
        if n % i//2+1 == 0:
            return False 
        return True
    
primes =[]

for n in ls:
    if is_prime(n):
        primes.append(n)
print(primes)

