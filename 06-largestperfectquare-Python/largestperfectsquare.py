# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

import math

def isPerfectSquare(n):
	if type(n) is int:
		if n < 0:
			return False
		elif math.sqrt(n) - int(math.sqrt(n)) == 0:
			return True
		else:
			return False
	else:
		return False

def largestperfectsquare(n):
	for x in range(n,0,-1):
		if isPerfectSquare(x):
			return x