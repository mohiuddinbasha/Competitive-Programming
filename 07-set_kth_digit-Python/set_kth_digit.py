# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag = False
	if n < 0:
		flag = True
		n = str(abs(n))
	else:
		n = str(n)
	n = n[::-1]
	n = n[:k]+str(d)+n[k+1:]
	n = n[::-1]
	value = int(n)
	if flag:
		return -1*value
	else:
		return value

