# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
    count = -1
    temp = 1
    while count < n:
        sqr = temp*2
        string = str(sqr)
        if sqr == temp:
            count += 1
        elif len(string) % 2 == 0:
            mid = len(string) // 2
            first = int(string[:mid])
            second = int(String[mid:])
            if first+second == temp:
                count += 1
        else:
            mid = len(string) // 2
            mid -= 1
            first = int(string[:mid])
            second = int(String[mid:])
            if first+second == temp:
                count += 1
    return temp - 1

