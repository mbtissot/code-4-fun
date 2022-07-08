"""
Finding the sum of the even Fibonacci numbers below a certain threshold
"""

a = 0  # First Fibonacci number
b = 1  # Second Fibonacci number
c = a + b  # Use this to calculate the next Fibonacci number

fibonacci = []  # In case you want to store them on a list
sum_even_fib = 0  # Initializing the variable 'sum_even_fib'
threshold = 4_000_000
while c < threshold:  # increments the fibonacci numbers below the threshold
	c = a + b
	if c < threshold:  # check if the number is bellow the threshold
		if c % 2 == 0:  # check if its even (you could change this to be mod n, n in naturals)
			sum_even_fib = sum_even_fib + c  # performs the sum
		a = b  # change a
		b = c  # change b

print(sum_even_fib)  # print the sum
