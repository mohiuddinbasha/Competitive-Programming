# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def onlyEvenDigits(l,p):
	if p >= len(l):
		return l
	else:
		v = 0
		n = l[p]
		print(n)
		while (n > 0):
			if v == 1 and n % 10 == 0:
				v = n % 10
			elif n % 10 == 0:
				v *= 10
				v += n % 10
			n = n / 10
		n = v
		print(n)
		v = 0
		while n > 0:
			if v == 1:
				v = n % 10
			else:
				v *= 10
				v += n % 10
			n = n / 10
		l[p] = v
	return onlyEvenDigits(l,p+1)

def fun_recursion_onlyevendigits(l):
		onlyEvenDigits(l,0) 
		return l