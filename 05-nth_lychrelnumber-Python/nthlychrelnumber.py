# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	temp = 196
	while count < n:
		boolean = True
		for i in range(100):
			t = int(str(temp)[::-1])
			temp = temp + t
			if str(temp) == str(temp)[::-1]:
				print(temp)
				boolean = False
				break
		print(boolean)
		if boolean:
			count += 1
		temp += 1
		break
	return temp - 1
print(nthlychrelnumbers(1))