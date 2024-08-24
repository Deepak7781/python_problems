'''
Given two polynomials represented by two arrays, write a function that adds given two polynomials. 

Example: 

Input:  A[] = {6, 10, 0, 5} 
        B[] = {4, 2, 41} 
Output: sum[] = {6, 14, 2, 6}

The first input array represents "6x^3 + 10x^2 + 0x^1 + 5"
The second array represents "4x^2 + 2x^1 + 1" 
And Output is "6x^3 + 14x^2 + 2x^1 + 6"

Algorithm:

1) Create a sum array sum[] of size equal to maximum of 'm' and 'n'
2) Copy A[] to sum[].
3) Traverse array B[] and do following for every element B[i]
          sum[i] = sum[i] + B[i]
4) Return sum[].

'''

def addTwoPolynamials(A,B):
    size = max(len(A),len(B))
    sum = [0 for i in range(size)]
    for i in range(len(A)):
        sum[i] = A[i]
    for i in range(len(B)):
        sum[i] += B[i]
    
    return sum

def printPoly(poly,n):
    for i in range(n):
        print(poly[i],end ="")
        if i != n-1:
            print(f"x^{n-1-i}",end="")
            print(" + ",end="")




A = [5,3,2]
B = [2,3,6]
m = len(A)
n = len(B)
print("Polynomial A: ",end="")
printPoly(A,m)
print()
print("Polynomial B: ",end="")
printPoly(B,n)
print()
Sum = addTwoPolynamials(A,B)
size = max(m,n)
print("Sum of Polynomials A and B : ",end = "")
printPoly(Sum,size)