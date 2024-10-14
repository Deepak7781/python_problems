def smallestMultiple(n):
    num = 1
    factors = []

    for n_fac in range(2,n+1):
        for fac in factors:
            if n_fac%fac == 0:
                n_fac = n_fac//fac
        
        num = num*n_fac
        factors.append(n_fac)
    return num

n = int(input("Enter number :"))
print(smallestMultiple(n))