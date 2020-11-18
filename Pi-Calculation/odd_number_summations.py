from math import sqrt,pi

no_of_terms = 10**6

sum1 = 0
for i in range(no_of_terms):
	term = (-1)**i/(2*i+1)
	sum1 += term;

pi_estimate_1 = 4*sum1

print(pi_estimate_1)

sum2 = 0
for i in range(no_of_terms):
	term = 1/(2*i+1)**2
	sum2 += term;

pi_estimate_2 = sqrt(8*sum2)

print(pi_estimate_2)

sum3 = 0
for i in range(no_of_terms):
	term = (-1)**i/(2*i+1)**3
	sum3 += term;

pi_estimate_3 = (32*sum3)**(float(1/3))

print(pi_estimate_3)


sum4 = 0
for i in range(no_of_terms):
	term = 1/(2*i+1)**4
	sum4 += term;

pi_estimate_4 = (96*sum4)**(float(1/4))

print(pi_estimate_4)	

sum5 = 0
for i in range(no_of_terms):
	term = (-1)**i/(2*i+1)**5
	sum5 += term;

pi_estimate_5 = (1536*sum5/5)**(float(1/5))

print(pi_estimate_5)

sum6 = 0
for i in range(no_of_terms):
	term = 1/(2*i+1)**6
	sum6 += term;

pi_estimate_6 = (960*sum6)**(float(1/6))

print(pi_estimate_6)
