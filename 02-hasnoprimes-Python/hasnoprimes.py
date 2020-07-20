# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isPrime(num):
	count = 0
	for i in range(1,num+1):
		if num % i == 0:
			count += 1
	return count == 2

def fun_hasnoprimes(l):
	for i in l:
		for x in i:
			print(x)
			if isPrime(x):
				return False
	return True

