def log2(n, x = 0):
    if n == 1:
        return x
    else:
        return log2(n//2,x+1)

print(log2(1))


