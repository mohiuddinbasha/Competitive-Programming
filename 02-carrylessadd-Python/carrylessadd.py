# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	s = ""
	while x > 0 and y > 0:
		first = x % 10
		second = y % 10
		v = first + second
		if v > 9:
			v -= 10
		if s == "":
			s = str(v)
		else:
			s = str(v) + s
		x = x // 10
		y = y // 10
	if x != 0:
		while x > 0:
			s = str(x % 10) + s
			x = x // 10
	if y != 0:
		while y > 0:
			s = str(y % 10) + s
			y = y // 10
	return int(s)

