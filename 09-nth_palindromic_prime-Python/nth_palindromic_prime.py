# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isPrime(n):
	count = 0
	for i in range(1, n+1):
		if n % i == 0:
			count += 1
	return count == 2

def isPalindrome(n):
	return str(n) == str(n)[::-1]

def fun_nth_palindromic_prime(n):
	index = 1
	count = -1
	while True:
		if isPalindrome(n) and isPrime(n):
			count += 1
		if count == n:
			break
		index += 1
	return index