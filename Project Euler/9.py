
def isPythagoras(a,b,c):
    return (a**2) + (b**2) == c**2
a = 1
num = []
while a < 999:
    b = 1
    while b < 999:
        c = 1 
        while c < 999:
            if a + b + c == 1000 and isPythagoras(a,b,c):
                num.extend(a,b,c)
            c += 1
        b += 1
    a += 1
        
print(num)
                
