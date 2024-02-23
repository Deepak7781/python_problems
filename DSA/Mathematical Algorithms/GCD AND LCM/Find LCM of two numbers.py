#To find the LCM of two numbers

def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b//gcd(a,b))

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

print("The LCM of",a,"and",b,"is",lcm(a,b))


#Another efficient way

def lcm(x,y):
    greater=max(x,y)
    smallest=min(x,y)
    for i in range(greater,(a*b)+1,greater):
        if i%smallest==0:
            return i
x=int(input("Enter the first number :"))
y=int(input("Enter the second number :"))

print("The LCM of",x,"and",y,"is",lcm(x,y))
