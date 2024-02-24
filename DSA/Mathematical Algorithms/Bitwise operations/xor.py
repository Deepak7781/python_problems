#Find XOR of two numbers without using xor operator

#method 1
'''def xor(x,y):
    return ((x|y)&(~x|~y))

x=int(input("Enter a number :"))
y=int(input("Enter a number :"))

print("XOR is ",xor(x,y))

#method2

def xor(x,y):
    return (x+y-(2*(x&y)))

x=3
y=5
print("XOR :",xor(x,y))'''

#method 3

def xor(x,y):
    return ((x|y)-(x&y))

x=int(input("Enter a number :"))
y=int(input("Enter another number :"))
print(x,"^",y,"is",xor(x,y))