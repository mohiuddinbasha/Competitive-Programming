# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

l = []
def recursion(string, p, last):
	if len(string)-1 == p:
		l.append(string)
		return
	val = string[p]
	for i in range(p,len(string)):
		if string[0] == last:
			print(string)
			string = list(string)
			t = string[-1]
			string[-1] = string[-2]
			string[-2] = t
			string = "".join(string)
			print(string)
		s = list(string)
		temp = s[i]
		s[i] = s[p]
		s[p] = temp
		s = "".join(s)
		print("s: ",s)
		recursion(s,p+1,last)

def getallpermutations(x):
	# Your code goes here
	recursion(x,0,x[-1])
	return [tuple(x) for x in l]
print(getallpermutations("abc"))