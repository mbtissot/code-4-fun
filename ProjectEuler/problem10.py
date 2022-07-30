from math import sqrt

def isNprime(n): # Checks if a number is prime. It checks up to sqrt(n)+1, since thats the largest factor
	# a number can have
	rangee = int(sqrt(n))+1 # This is here for the purpose of debugging (which took me ~30min)
	for i in range(2, rangee+1):
		if n%i==0:
			return False
	return True

def sumprimes(threshold): # Loops through numbers up to the threshold, and if it is prime, adds it to
	# 'soma', and then returns 'soma'.
	soma = 2
	for j in range(2, threshold+1):
		if isNprime(j):
			soma = soma + j
	return soma

print(sumprimes(2000000))