# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count == 2

def fun_nth_smithnumber(n):
    count = -1
    temp = 2
    while count < n:
        if not isPrime(temp):
            # print(temp)
            s = []
            for i in range(2,temp):
                if isPrime(i) and temp % i == 0:
                    q = temp // i
                    s.append(str(q))
            s = "".join(s)
            t = list(s)
            print(t)
            s = 0
            for x in t:
                s += int(x)
            temp_sum = 0
            d = temp
            while d > 0:
                temp_sum += d % 10
                d = d // 10
            if s == temp_sum:
                count += 1
        temp += 1
    return temp - 1
print(fun_nth_smithnumber(0))