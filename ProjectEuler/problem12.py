from math import sqrt

def triangular(n): # Creates the nth triangular number
	return sum(range(n+1))


def divisors(n): # Counts the divisors of a number
	divisorcount = 2
	for i in range(2, int(n/2)+1):
		if n%i==0:
			divisorcount = divisorcount + 1
	return divisorcount

threshold = 7 # How many divisors do we want? In the example: 5. In the problem: 500
# I am definetely not running this up to 500 divisors. It'll take ages.
i = 1
while True:
	divs = divisors(triangular(i))
	if divs<threshold:
		pass
	else:
		print(triangular(i), divs)
		break
	i = i+1


