# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	count = -1
	temp = 1
	while count < n:
		sqr = temp**2
		s_temp = str(temp)
		s_sqr = str(sqr)
		t = int(s_sqr[(-1*len(s_temp)):])
		if temp == 0:
			count += 1
		temp += 1
		# print(count)
		break
	return temp - 1
print(nthautomorphicnumbers(2))