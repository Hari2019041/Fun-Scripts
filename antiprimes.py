from math import sqrt

def find_no_of_factors(N):
	factors = []

	for i in range(1, int(sqrt(N)+1)):
		if N%i == 0:
			if N/i == i:
				factors.append(i)
			else:
				factors.append(i)
				factors.append(int(N/i))

	return len(factors)

N = 10**6

max_no_of_factors = [0]
current_antiprime = 0
list_of_antiprimes = []

for i in range(1, N+1):
	if  find_no_of_factors(i) > max_no_of_factors[-1]:
		max_no_of_factors.append(find_no_of_factors(i))
		current_antiprime = i;
		list_of_antiprimes.append(i)

print(list_of_antiprimes)
print(max_no_of_factors)

