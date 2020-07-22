# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = -1
	temp = 1
	while count < n:
		s = temp**5
		s = str(s)
		if (all(str(x) in s for x in range(10))):
			count += 1
		temp += 1
	return temp - 1
print(nthwithproperty309(0))