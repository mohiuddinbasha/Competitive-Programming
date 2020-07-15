# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	d = {}
	while n > 0:
		val = n % 10
		if val in d:
			d[val] += 1
		else:
			d[val] = 1
		n = n // 10
	(num,c) = (0,0)
	for x in d.keys():
		if d[x] > c or (d[x] == c and x < num):
			(num,c) = (x,d[x])
	return num