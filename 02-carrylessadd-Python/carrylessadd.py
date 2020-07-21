# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	s = 0
	zero = False
	count = 0
	while x > 0 and y > 0:
		first = x % 10
		second = y % 10
		v = first + second
		if v > 9:
			v = 10-v
		if v == 0:
			zero = True
			count += 1
		if s == 0:
			s = v
		else:
			if zero:
				s += v
				s *= (10**count)
				zero = False
				count = 0
			else:
				s *= 10
				s += v
		x = x // 10
		y = y // 10
	if x != 0:
		while x > 0:
			if zero:
				s += x % 10
				s *= (10**count)
				zero = False
				count = 0
			else:
				s *= 10
				s += x % 10
			x = x // 10
	if y != 0:
		while y > 0:
			if zero:
				s += x % 10
				s *= (10**count)
				zero = False
				count = 0
			else:
				s *= 10
				s += x % 10
			y = y // 10
	s = str(s)
	s = s[::-1]
	return int(s)


