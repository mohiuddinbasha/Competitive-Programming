# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isAutomorphic(temp):
	s_temp = str(temp)
	sqr = temp**2
	s_sqr = str(sqr)
	t = s_sqr[(-1*len(s_temp)):]
	return s_temp == t

def nthautomorphicnumbers(n):
	# Your code goes here
	if n == 1 or n == 2:
		return n-1
	count = 2
	temp1 = 5
	temp2 = 6
	while count < n:
		counter = 0
		while True:
			s1 = str(counter)+str(temp1)
			if isAutomorphic(int(s1)):
				break
			counter += 1
		temp1 = int(str(counter)+str(temp1))
		counter = 0
		while True:
			s2 = str(counter)+str(temp2)
			if isAutomorphic(int(s2)):
				break
			counter += 1
		temp2 = int(str(counter)+str(temp2))
		count += 2
	small = big = -1
	if temp1 < temp2:
		small = temp1
		big = temp2
	else:
		small = temp2
		big = temp1
	if n % 2 != 0:
		return small
	else:
		return big
print(nthautomorphicnumbers(4))