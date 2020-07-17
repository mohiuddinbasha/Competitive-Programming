# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.


def fun_getaverage(s):
	g = s.split(",")
	l = []
	for x in g:
		if x.isnumeric():
			l.append(int(x))
	if len(l) == 0:
		return 0.0
	else:
		sum = 0
		for x in l:
			sum += x
		return sum/len(l)

