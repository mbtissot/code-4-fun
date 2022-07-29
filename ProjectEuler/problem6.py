'''
The sum of the first 10 natural numbers squared is (1² + 2² + ... + 10²) = 385
The square of the sum of the first 10 natural numbers is (1 + 2 + ... + 10)² = 3025
The difference between them is 3025-385 = 2640.

Find the difference if you were to sum the first 100 natural numbers.
'''
def sumsquares(n): # Sum of squares
	soma = 0
	for i in range(n+1):
		soma = soma + i**2
	return soma

def squareSum(n): # Square of sum 
	soma = 0
	for i in range(n+1):
		soma = soma + i
	return soma**2

def diff(n): # Difference between them
	return squareSum(n) - sumsquares(n)

# print(diff(100)) # If you uncomment this, you'll get spoiler of the answer.