def ds(n):
	""" This function tests if in 'n' any of the digits is the sum of the rest. If so, return True.
	If not, return False.

	Example 1: ds(325) -> Is 3 = 5+2? No. Is 2 = 3+5? No. Is 5 = 3+2? Yes. So this function will return True.
	Example 2: ds(124) -> Is 1 = 2+4? No. Is 2 = 1+4? No. Is 4 = 1+2? No. So this function will return False
	"""
	num = str(n)
	for index in range(len(num)):
		soma = 0
		string = num[:index] + num[index+1:]
		for d in string:
			soma = soma + int(d)
		if int(num[index])==soma:
			return True
	return False

# Now we will define S(n) = Sum of all the ds() numbers with 'n' digits or less.


# First test: Is S(3) = 63270, as the prompt stated?
'''dslist = []
listanums = []
truefalse = []
for i in range(1, 10**4):
	num = str(i)
	nums = {str(i):num.count(str(i)) for i in range(10)}
	if nums in listanums and truefalse[listanums.index(nums)]==True:
		dslist.append(i)
	else:
		if ds(i)*()
			dslist.append(i)
			truefalse.append(True)
		else:
			truefalse.append(False)
		listanums.append(nums)
print(sum(dslist))'''   # 4.5 seconds with range 10⁴.

'''
dslist = []
listanums = []
truefalse = []
for i in range(1, 10**4): # runs through numbers
	num = str(i) # rewrites the number as a string
	nums = {str(i):num.count(str(i)) for i in range(10)} # creates dict with how many of each digit there is in the number 
	if truefalse[listanums.index(nums)]==True: # tests if it was true for some other number with same digits
		dslist.append(i) # if so, append it
	else:
		if ds(i):
			dslist.append(i)
			truefalse.append(True)
		else:
			truefalse.append(False)
		listanums.append(nums)
print(sum(dslist)) # 449 ms for 10⁴
'''

dslist = []
for i in range(1, 10**3):
	#num = str(i) # rewrites the number as a string
	#nums = {str(i):str(i).count(str(i)) for i in range(10)}
	if ds(i):
		dslist.append(i)

print(sum(dslist)) # 6s for 10⁶ # 3149685 for 10⁴ = 85 mod 100

# This is not optimized at all. Ideally, we would scoop all the numbers with the same digits into one iteration
# And compute only numbers with distinct digits. So this is to be done in the future.
'''for i in range(1, 10**7):
	if ds(i):
		dslist.append(i)

print(sum(dslist))

Both the tests for N = 3, and N = 7 gave us the right answers. However, it took 84s to compute S(7).
Computing S(2020) would take "i don't even wanna think about it" seconds, which i don't have. So i'll leave
this at this point, and try to optimize it in the future. I know my logic works, so i think i will
leave this here.
'''