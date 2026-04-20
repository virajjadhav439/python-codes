
from functools import reduce

n = int(input("Enter a number: "))

factorial = reduce(lambda x, y: x * y, range(1, n + 1), 1)

print("Factorial:", factorial)