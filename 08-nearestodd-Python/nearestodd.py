# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	real = int(n)
	decimal = n - real
	if real % 2 != 0:
		return real
	else:
		if (real+1)-n < n-(real-1):
			return real+1
		else:
			return real-1


