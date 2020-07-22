# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def isPrime(n):
    count = 0
    for x in range(1,n+1):
        if n % x == 0:
            count += 1
    return count == 2

def isHappyNumber(n):
    temp = n
    boolean = False
    while True:
        s = 0
        while temp > 0:
            s += (temp % 10)**2
            temp = temp // 10
        if s == 1:
            boolean = True
            break
        if s == 4:
            break
        temp = s
    return boolean

def ishappyprimenumber(n):
    # Your code goes here
    return isPrime(n) and isHappyNumber(n)