def is_prime(p):
	for i in range(2, p):
		if p%i == 0:
			return False

	return True

def find_primes(N):
	primes = []
	i = 2
	while (len(primes) < N):
		if is_prime(i):
			primes.append(i)
		i += 1

	return primes

def check_property(primes):
	total = 0
	for prime in primes:
		total += prime**2

	return int(total)%len(primes) == 0

candidates = []

for i in range(1, 101):
	if check_property(find_primes(i)):
		candidates.append(i)

print(candidates)


