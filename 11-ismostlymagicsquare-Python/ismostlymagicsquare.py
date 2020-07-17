# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	count = sum[a[0]]
	for x in range(len(a)-1):
		if sum[x] != sum[x+1]:
			return False
	for x in range(len(a)):
		temp = 0
		for y in range(len(a)):
			temp += a[y][x]
		if temp != count:
			return False
	i = 0
	j = 0
	temp = 0
	while i < len(a):
		temp += a[i][j]
		i += 1
		j += 1
	if temp != count:
		return False
	i = temp = 0
	j = len(a)-1
	while i < len(a):
		temp += a[i][j]
		i += 1
		j -= 1
	if temp != count:
		return False
	return True
