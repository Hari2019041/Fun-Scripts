from math import gcd, sqrt, pi
from random import randint

NO_OF_TRIALS = 10**6
RANGE_OF_NUMBERS = 10**9

count = 0
for i in range(NO_OF_TRIALS):
    a = randint(1, RANGE_OF_NUMBERS + 1)
    b = randint(1, RANGE_OF_NUMBERS + 1)
    count += 1 if gcd(a, b) == 1 else count

probability = count / NO_OF_TRIALS

pi_estimate = sqrt(6 / probability)

absolute_error = abs(pi - pi_estimate)
relative_error = absolute_error / pi
percentage_error = relative_error * 100

print("PI ESTIMATE:", pi_estimate)
print("ABSOLUTE ERROR:", absolute_error)
print("PERCENTAGE ERROR:", percentage_error, "%")
