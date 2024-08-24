'''
Find the LCM of two numbers without using the gcd 

Approach : The approach is to start with the largest of the 2 numbers and 
keep incrementing the larger number by itself till smaller number perfectly divides the resultant.

'''

def LCM(n1,n2):
    lar = max(n1,n2)
    small = min(n1,n2)
    i = lar
    while (1):
        if i%small == 0:
            return i
        i += lar

n1,n2 = map(int, input("Enter two numbers :").split())
print(LCM(n1,n2))
