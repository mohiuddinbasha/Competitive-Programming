# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	l = []
	for x in L:
		l.append(sum(x))
	actual_sum = 0
	flaw_xposition = 0
	for x in range(0,len(L)):
		if l.count(sum(L[x])) > 1:
			actual_sum = sum(L[x])
		else:
			flaw_xposition = x
	l = []
	for x in range(len(L)):
		s = 0
		for y in range(len(L)):
			s += L[y][x]
		l.append(s)
	actual_sum = 0
	flaw_yposition = 0
	for x in range(len(L)):
		s = 0
		for y in range(len(L)):
			s += L[y][x]
		if l.count(s) > 1:
			actual_sum = s
		else:
			flaw_yposition = x

	l = L[flaw_xposition]
	v = actual_sum - (sum(l)-l[flaw_yposition])
	l[flaw_yposition] = v
	L[flaw_xposition] = l
	return L