# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    count = -1
    temp = 1
    while count < n:
        boolean = True
        s = str(temp)
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                boolean = False
                break
        if boolean:
            count += 1
        temp += 1
    return temp - 1
        