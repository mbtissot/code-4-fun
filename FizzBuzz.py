# With loads of 'ifs'
'''
for i in range(1, 101):
	if i%3==0 and i%5!=0:
		print('Fizz')
	elif i%3!=0 and i%5==0:
		print('Buzz')
	elif i%3==0 and i%5==0:
		print('FizzBuzz')
	else:
		print(i)
'''

#Without ifs:

for i in range(1, 101):
	print('Fizz'*(i%3==0 and i%5!=0) + 'Buzz'*(i%3!=0 and i%5==0)
		+ 'FizzBuzz'*(i%3==0 and i%5==0) + str(i)*(i%3!=0 and i%5!=0))
