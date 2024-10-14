'''
The prime factors of 13195 are 5,7,13,29.
What is the largest prime factor of the number 600851475143?
'''
from math import floor,sqrt

def isPrime(n):
    if n == 1:
       return False
    elif n < 4:
       return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        while f<=r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f = f+6
        return True

num = int(input())

fac = num // 2 +1 

for i in range(fac,1,-1):
    if isPrime(i):
        if num % i == 0:
            print(i)
            