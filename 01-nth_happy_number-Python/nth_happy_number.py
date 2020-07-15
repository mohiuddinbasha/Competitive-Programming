# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def is_HappyNumber(n):
	if n == 0 or n == 4:
		return False
	elif n == 1:
		return True
	else:
		v = 0
		while n > 0:
			v += (n % 10)**2
			n = n // 10
		return is_HappyNumber(v)

def fun_nth_happy_number(n):
	temp = 1
	while n <= 0:
		print("temp: "+temp)
		if is_HappyNumber(temp):
			n -= 1
		temp += 1
	return temp-1
print(fun_nth_happy_number(1))
