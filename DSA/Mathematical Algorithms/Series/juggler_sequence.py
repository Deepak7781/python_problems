'''
Juggler Sequence is a series of integer number in which the first term starts with a positive 
integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation : 
a_{k+1}=\begin{Bmatrix} \lfloor a_{k}^{1/2} \rfloor & for \quad even \quad a_k\\ \lfloor a_{k}^{3/2} \rfloor & for \quad odd \quad a_k \end{Bmatrix}
Juggler Sequence starting with number 3: 
3, 5, 11, 36, 6, 2, 1
Juggler Sequence starting with number 9: 
9, 27, 140, 11, 36, 6, 2, 1
Given a number n we have to print the Juggler Sequence for this number as the first term of the sequence. 
Examples: 
 

Input: 9
Output: 9, 27, 140, 11, 36, 6, 2, 1
We start with 9 and use above formula to get
next terms.

Input: 6
Output: 6, 2, 1

'''
import math

def juggler(n):
    a = n
    print(a,end=" ")
    while a != 1:
        b = 0
        if a%2 == 0:
            b = int(math.floor(math.sqrt(a)))
        else:
            b = int(math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a)))
        print(b,end=" ")
        a = b
juggler(9)

