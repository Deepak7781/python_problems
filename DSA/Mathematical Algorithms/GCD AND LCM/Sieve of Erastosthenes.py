#Sieve of eratosthenes

def sieve_prime(n):
    prime=[0 for i in range(n+1)]

    for i in range(2,n+1):
        if prime[i]==0:
            for j in range(i*i,n+1,i):
                prime[j]=1
    for i in range(2,n+1):
        if prime[i]==0:
            print(i,end=' ')

n=int(input("Enter the number :"))
sieve_prime(n)
                
