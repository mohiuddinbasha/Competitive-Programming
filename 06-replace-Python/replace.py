# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	for x in range(0,len(s1),1):
		if s1[x:len(s2)-1] == s2:
			s1 = s1[:x]+s3+s1[x+len(s2):]
	return s1

print(fun_replace("helloworld123", "hello", "345"))

