# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
import math

def isPrime(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    x = 5
    while x <= math.sqrt(n):
        if n % x == 0 or n % (x+2) == 0:
            return False
        x += 6
    return True

def fun_nth_uglynumber(n):
    count = 0
    if n == 0:
        return 1
    temp = 2
    while count < n:
        # print(temp)
        l = [2, 3, 5]
        boolean = True
        for i in range(2,temp):
            if isPrime(i) and n % i == 0 and i not in l:
                boolean = False
                break
        # print(boolean)
        if boolean:
            count += 1
        temp += 1
    return temp - 1
print(fun_nth_uglynumber(8))
# for i in range(10):
#     print(fun_nth_uglynumber(i))
