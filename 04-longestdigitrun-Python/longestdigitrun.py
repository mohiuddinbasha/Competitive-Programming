# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n = abs(n)
	max_num = 0
	max_count = 0
	num = 0
	count = 0
	n = str(n)
	for x in n:
		if count == 0:
			num = x
			max_num = x
			count = 1
			max_count = 1
		elif num == x:
			count += 1
		else:
			if count > max_count:
				max_count = count
				max_num = num
			elif count == max_count:
				if num < max_num:
					max_num = num
			num = x
			count = 1
	if count > max_count:
		max_count = count
		max_num = num
	elif count == max_count:
		if num < max_num:
			max_num = num
	return int(max_num)
				