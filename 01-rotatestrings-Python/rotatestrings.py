# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def helperfunc(s, n):
	while (n > len(s)):
			n -= len(s)
	n = n - 1
	s = s[n+1:]+s[:n+1]
	return s

def fun_rotatestrings(s, n):
	if n > 0:
		return helperfunc(s,n)
	else:
		n = abs(n)
		s = s[::-1]
		s = helperfunc(s,n)
		return s[::-1]

