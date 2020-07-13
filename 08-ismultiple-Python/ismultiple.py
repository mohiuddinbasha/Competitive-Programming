# Write the function isMultiple that takes two int values m and n 
# and returns True if m is a multiple of n and False otherwise. 
# Note that 0 is a multiple of every integer including itself. 
# Also, you should make constructive use of the isFactor function you just wrote above.

def isFactor(f, n):
	if n == 0:
		return True
	elif f == 0:
		return False
	else:
		return n % f == 0

def fun_ismultiple(m, n):
	return isFactor(n, m) # replace with your solution
