# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

from itertools import permutations

l = []
def recursion(string, p):
	if len(string)-1 == p:
		l.append(string)
		return
	val = string[p]
	for i in range(p,len(string)):
		s = list(string)
		temp = s[i]
		s[i] = s[p]
		s[p] = temp
		s = "".join(s)
		recursion(s,p+1)

def getallpermutations(x):
	# Your code goes here
	# l.clear()
	# recursion(x,0)
	# out = [tuple(x) for x in l] 
	# return sorted(out)
	return list(permutations(x, r=len(x)))