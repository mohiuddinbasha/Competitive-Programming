# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isPrime(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0:
			count += 1
	return count == 2

def nthpowerfulnumber(n):
	# Your code goes here
	if n == 0:
		return 1
	count = 0
	temp = 2
	while count < n:
		l = []
		for x in range(1, temp):
			if temp % x == 0 and isPrime(x):
				l.append(x)
		if(all(temp % x**2 == 0 for x in l)):
			count += 1
		temp += 1
	return temp - 1

