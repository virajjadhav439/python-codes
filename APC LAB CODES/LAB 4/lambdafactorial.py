from functools import reduce

n = 5

factorial = reduce(lambda a, b: a * b, range(1, n + 1))

print(factorial)
