# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.

import math

def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count == 2

def fun_nth_lefttruncatableprime(n):
    count = -1
    temp = 2
    while count < n:
        if isPrime(temp):
            boolean = True
            t = temp
            while t > 0:
                if not isPrime(t % 10):
                    boolean = False
                t = t // 10
            if boolean:
                count += 1
        temp += 1
    return temp - 1

print(fun_nth_lefttruncatableprime(1))
