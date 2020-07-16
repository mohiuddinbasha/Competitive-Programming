# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	output = ""
	l = len(s1) if len(s1) < len(s2) else len(s2)
	for x in range(0,l,1):
		output += s1[x]
		output += s2[x]
	output += s2[l:]
	output += s1[l:]
	return output
 	