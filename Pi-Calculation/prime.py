from random import randint
import math

N = 1000000
count = 0

for i in range(N):
    a = randint(1, N+1)
    b = randint(1, N+1)
    if math.gcd(a, b) == 1:
        count += 1

pi_estimate = math.sqrt(6*N/count)

absolute_error = math.pi - pi_estimate
percentage_error = (absolute_error/math.pi)*100

print(math.pi)
print(pi_estimate)

print(percentage_error)
