# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

l = []
def recursion(string, p):
	if len(string)-1 == p:
		return
	val = string[p]
	for i in range(p,len(string)):
		s = string[:i] + val + string[i+1:]
		print(s)
		# l.append(s)
		# recursion(s,p+1)

def getallpermutations(x):
	# Your code goes here
	recursion(x,0)
	return [tuple(x) for x in l]
print(getallpermutations("abc"))
