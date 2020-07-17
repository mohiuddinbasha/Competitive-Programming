# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	#(ax**2+bx+c)(px**2+qx+r) = apX**4+(aq+bp)X**3+(ar+bq+cp)X**2+(br+cq)X+cr/////
	a = b = c = 0
	p = q = r = 0
	if len(p1) == 3:
		a = p1[0]
		b = p1[1]
		c = p1[2]
	elif len(p1) == 2:
		b = p1[0]
		c = p1[1]
	else:
		c = p1[0]
	if len(p2) == 3:
		p = p2[0]
		q = p2[1]
		r = p2[2]
	elif len(p2) == 2:
		q = p2[0]
		r = p2[1]
	else:
		r = p2[0]
	if len(p1) == len(p2) == 3:
		l = [a*p,(a*q+b*p),(a*r+b*q+c*p),(b*r+c*q),c*r]
	elif ((len(p1) == 3 and len(p2) == 2) or (len(p2) == 3 and len(p1) == 2)):
		l = [(a*q+b*p),(a*r+b*q+c*p),(b*r+c*q),c*r]
	elif len(p1) == len(p2) == 2:
		l = [(a*r+b*q+c*p),(b*r+c*q),c*r]
	elif ((len(p1) == 2 and len(p2) == 1) or (len(p2) == 2 and len(p1) == 3)):
		l = [(b*r+c*q),c*r]
	elif len(p1) == len(p2) == 1:
		l = [c*r]
	return l
	