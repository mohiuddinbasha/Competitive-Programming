# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
	count = 0
	for i in range(1,n+1,1):
		if n % i == 0:
			count += 1
	return count == 2

def isHappyNumber(n):
	if n == 0 or n == 4:
		return False
	elif n == 1:
		return True
	else:
		val = 0
		while n > 0:
			val += (n % 10)**2
			n = n // 10
		return isHappyNumber(val)

def fun_nth_happy_prime(n):
	temp = 1
	while n >= 0:
		if isHappyNumber(n) and isPrime(n):
			n -= 1
		temp += 1
	return temp-1

print(isPrime(7))