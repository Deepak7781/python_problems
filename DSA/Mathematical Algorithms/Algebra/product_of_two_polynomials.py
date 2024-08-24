'''
Given two polynomials represented by two arrays, write a function that multiplies given two polynomials. 

Example: 

Input:  A[] = {6, 10, 0, 5} 
        B[] = {4, 2, 1} 
Output: prod[] = {24, 52, 26, 30, 10, 5}

The first input array represents "6x^3 + 10x^2 + 0x^1 + 5"
The second array represents "4x^2 + 2x^1 + 1" 
And Output is "24x^5 + 52x^4 + 26x^3 + 30x^2 + 10x^1 + 5"

Algorithm :
1) Create a product array prod[] of size m+n-1.
2) Initialize all entries in prod[] as 0.
3) Traverse array A[] and do following for every element A[i]
...(3.a) Traverse array B[] and do following for every element B[j]
          prod[i+j] = prod[i+j] + A[i] * B[j]
4) Return prod[].
'''

def product(A,B):
    m = len(A)
    n = len(B)
    prod  = [0] * (m+n-1)

    for i in range(m):
        for j in range(n):
            prod[i+j] += A[i] * B[j]
    return prod

def printPoly(poly,n):
    for i in range(n):
        print(poly[i],end ="")
        if i != n-1:
            print(f"x^{n-1-i}",end="")
            print(" + ",end="")
    print()
    
A = [6, 10, 0, 5]
B = [4, 2, 1]
print("Polynomial A:")
printPoly(A,len(A))
print("Polynomial B:")
printPoly(B,len(B))
product = product(A,B)
print("Product of polynomial A and B:")
printPoly(product,len(A)+len(B)-1)
