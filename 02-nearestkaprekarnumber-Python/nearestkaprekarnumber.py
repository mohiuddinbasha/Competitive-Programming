# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    below_n = 0
    after_n = 0
    temp = n
    while below_n == 0:
        sqr = temp**2
        s = str(sqr)
        if(any(int(s[x:]) != 0 and int(s[:x])+int(s[x:]) == temp for x in range(1,len(s)))):
            below_n = temp
        temp -= 1
    temp = n
    while after_n == 0:
        sqr = temp**2
        s = str(sqr)
        if(any(int(s[x:]) != 0 and int(s[:x])+int(s[x:]) == temp for x in range(1,len(s)))):
            after_n = temp
        temp += 1
    diff1 = n - below_n
    diff2 = after_n - n
    if diff1 < diff2:
        return below_n
    elif diff1 > diff2:
        return after_n
    else:
        return below_n
    
