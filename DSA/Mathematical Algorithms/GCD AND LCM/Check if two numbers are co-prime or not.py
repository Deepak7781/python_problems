#Co-Prime Numbers
'''
Two  numbers are said to be co-prime or mutually prime if the greatest common divisor of them is
'''

def gcd(a,b):
    if ((a==0 and b==1) or (a==1 and b==0)):
        return 1
    if(a==0 or b==0):
        return 0
    
    if(a==b):
        return a

    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

def coprime(a,b):
    if(gcd(a,b)==1):
        print("Co-prime")
    else:
        print("Not co-prime")

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
coprime(a,b)
