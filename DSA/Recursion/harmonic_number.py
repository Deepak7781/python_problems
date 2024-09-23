def harmonic_number(n):
    if n == 1:
        return 1
    else:
        return (1/n)+harmonic_number(n-1)

n = int(input("Enter the n :"))
print(harmonic_number(n))