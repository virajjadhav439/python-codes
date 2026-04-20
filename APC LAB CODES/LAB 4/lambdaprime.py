
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]

primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, x)), numbers))

print("Prime numbers:", primes)