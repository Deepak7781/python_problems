#Naive approach for GCD of teo numbers
'''
def gcd(a,b):
    result=min(a,b)
    while result:
        if a%result==0 and b%result==0:
            break
        result-=1
    return result

a=int(input("Enter the fist number :"))
b=int(input("Enter the second number :"))
print(f"The GCD of {a} and {b} is {gcd(a,b)}")
'''

#Euclidean Algorithm for GCD of two numbers

'''
The idea of this is, the GCD of two numbers dosen't change if the smaller number is subtracted from the bigger number. This is the Euclidean algorithm by subtraction'''

def gcd(a,b):
    if(a==0):
        return b
    if b==0:
        return a
    #base case
    if a==b:
        return a

    if a>b:
        if a%b==0:
            return b
        return gcd(a-b,b)
    if b%a==0:
        return a
        
    return gcd(a,b-a)

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The GCD of",a ,"and",b,"is",gcd(a,b))


#Optimization using division
'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
if(gcd(a,b)):
    print(gcd(a,b))
else:
    print('not found')
'''
#Iterative implementation for GCD of two numbers using Euclidean Algorithm
'''
def gcd(a,b):
    while(a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
if(gcd(a,b)):
    print(gcd(a,b))
else:
    print("not found")

'''
#Using In-built function
'''
import math

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

gcd_result=math.gcd(a,b)
print(gcd_result)
'''
