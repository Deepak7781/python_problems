#Find XOR of two numbers without using xor operator

def xor(x,y):
    return ((x|y)&(~x|~y))

x=int(input("Enter a number :"))
y=int(input("Enter a number :"))

print("XOR is ",xor(x,y))