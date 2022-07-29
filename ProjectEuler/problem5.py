"""
2520 is the smallest number that is divisible without
any remainders by all the numbers from 1 to 10.
What is the smallest number that does the same from 1 to 20?
"""
checklist = [3, 5, 9, 11, 13, 14, 16, 17, 19]

# If a number divides 16, it divides 2, 4 and 8. So i don't need to check them
# If a number divides 5 and 16, it divides 10, 20
# If a number divides 3 too, it will divide 6, 12, 15, 18
# If a number divider 14, it kills 7

# The remaining list is the following:

checklist = [3, 5, 9, 11, 13, 14, 16, 17, 19]
# The first time i ran this code i did it up to 1billion, but then reduced it because i already knew the answer
for i in range(0, 250000000, 10): # I only need to check multiples of ten, so step=10.
	count = 0
	for k in checklist:
		if i%k!=0:
			break
		else:
			count = count+1
			if count == len(checklist):
				print(i)