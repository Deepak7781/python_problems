import math
def gcd(a,b):
    if a==0:
        return b
    return math.gcd(b%a,a)
def countPairs(G,L):
    count=0
    p=G*L
    for a in range(G,L+1):
        if (p%a==0 and math.gcd(a,p//a))==G:
            count+=1
    return count

G=int(input("Enter the GCD :"))
L=int(input("Enter the LCM :"))
print("Pairs :",countPairs(G,L))
