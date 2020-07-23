# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	temp = 1
	while count < n:
		boolean = True
		s = temp
		for i in range(100):
			t = int(str(s)[::-1])
			s = s + t
			if str(s) == str(s)[::-1]:
				boolean = False
				break
		if boolean:
			count += 1
		temp += 1
	return temp - 1