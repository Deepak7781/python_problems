#Count numbers in range 1 to n which are divisible by x not y

def countNumbers(x,y,n):
    count=0
    for i in range(1,n+1):
        if((i%x==0) and (i%y!=0)):
            count+=1
    return count

x=int(input("Enter the first divisor :"))
y=int(input("Enter the second divisor :"))
n=int(input("Enter the number :"))

print(countNumbers(x,y,n))


#Efficient method to solve this problem

from math import gcd

def count_Numbers(x,y,n):

    divisibleBy_x=int(n/x)
    divisibleBy_y=int(n/y)
    LCM=int(x*y/gcd(x,y))
    divisibleBy_LCM=int(n/LCM)

    divisibleBy_x_or_y=(divisibleBy_x +divisibleBy_y - divisibleBy_LCM)
    divisibleBy_x_not_y=(divisibleBy_x_or_y - divisibleBy_y)

    return divisibleBy_x_not_y

x=int(input("Enter the first divisor: "))
y=int(input("Enter the second divisor :"))
n=int(input("Enter the number :"))

print(count_Numbers(x,y,n))
    
