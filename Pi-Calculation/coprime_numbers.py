from math import gcd, sqrt, pi
from random import randint

no_of_trials = 10**6
range_of_numbers = 10**9

count = 0
for i in range(no_of_trials):
	a = randint(1, range_of_numbers+1)
	b = randint(1, range_of_numbers+1)
	if gcd(a,b) == 1:
		count +=1;

probability = count/no_of_trials

pi_estimate = sqrt(6/probability)

absolute_error = abs(pi - pi_estimate) 
relative_error = absolute_error/pi
percentage_error = relative_error*100

print("PI ESTIMATE:", pi_estimate)

print("ABSOLUTE ERROR:", absolute_error)
print("PERCENTAGE ERROR:", percentage_error, "%")