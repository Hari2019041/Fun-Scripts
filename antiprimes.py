"""
    Antiprime is a number which has the the maximum number of factors
    than every number less than it.
    This program finds out the antiprimes.
"""

from math import sqrt


def find_no_of_factors(N):
    no_of_factors = 0
    for i in range(1, int(sqrt(N) + 1)):
        if N % i == 0:
            no_of_factors += 1 if N / i == i else 2

    return no_of_factors


N = 10**5

max_no_of_factors = [0]
current_antiprime = 0
list_of_antiprimes = []

for i in range(1, N + 1):
    no_of_factors = find_no_of_factors(i)
    if no_of_factors > max_no_of_factors[-1]:
        max_no_of_factors.append(no_of_factors)
        current_antiprime = i
        list_of_antiprimes.append(i)

print(list_of_antiprimes)
print(max_no_of_factors)
