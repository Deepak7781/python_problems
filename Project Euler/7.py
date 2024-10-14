import math

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f = f + 6
        return True

n = int(input().strip())
count = 1
num = 1
while count < n:
    num += 2
    if isPrime(num):
        count += 1
print(num)