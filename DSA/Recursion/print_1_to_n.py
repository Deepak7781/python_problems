def printnumbers(n):
    if n>0:
        printnumbers(n-1)
        print(n, end=" ")
        

printnumbers(10)