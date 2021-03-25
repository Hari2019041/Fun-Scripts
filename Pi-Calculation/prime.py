from random import randint
from math import gcd, sqrt, pi

N = 1000000
count = 0

for i in range(N):
    a = randint(1, N + 1)
    b = randint(1, N + 1)
    count += 1 if gcd(a, b) == 1 else 0

pi_estimate = sqrt(6 * N / count)

absolute_error = pi - pi_estimate
percentage_error = (absolute_error / pi) * 100

print(pi)
print(pi_estimate)

print(percentage_error)
