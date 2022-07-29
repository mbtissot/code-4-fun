"""
Finding the biggest palindrome number that is product of two 3-digit numbers
"""

def check_palindrome(x):  # Palindrome checker
	number_string = str(x)
	if number_string[::-1] == number_string:
		return True
	else:
		return False


# palindromes = []  # In case you want a list of palindromes
max_num = 0  # Max number
factor1 = 0  # Factor 1
factor2 = 0  # Factor 2

"""Finding the largest palindrome product of two 3-digit numbers"""
for i in range(999, 99, -1):  # 3 digit numbers decreasing, starting from 999
	for j in range(999, 99, -1):  # Same ^
		number = i * j
		if check_palindrome(number) is True:
			if number > max_num:
				max_num = number
				factor1 = i
				factor2 = j
			# palindromes.append(number) #if you want a list every palindrome number
			# print(f'O numero {number} é palíndrome e é produto de {i} e {j}')
		else:
			continue

print(f'The largest palindrome number product of two 3-digits numbers is {max_num}, and its factors are ({factor1},{factor2})')
