# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = str(abs(n))
	for x in range(0,len(n)-1,1):
		if n[x] == n[x+1]:
			return True
	return False
