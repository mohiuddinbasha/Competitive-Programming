# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math

def distance(x1, y1, x2, y2):
	value = (x2-x1)**2+(y2-y1)**2
	return math.sqrt(value)

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = distance(x1,y1,x2,y2)
	b = distance(x2,y2,x3,y3)
	c = distance(x1,y1,x3,y3)
	l = max(a,b,c)
	if a == l:
		return a == math.sqrt(b**2+c**2)
	elif b == l:
		return b == math.sqrt(a**2+c**2)
	else:
		return c == math.sqrt(a**2+b**2)
