# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0:
			count += 1
	return count == 2

def check(n):
	total = 0
	while n > 0:
		total += n % 10
		n = n // 10
	return isPrime(total)

def fun_nth_additive_prime(n):
	count = -1
	index = 1
	while True:
		if isPrime(index) and check(index):
			count += 1
		if count == n:
			break
		index += 1
	return index
print(fun_nth_additive_prime(0))