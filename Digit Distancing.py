#QUESTION
'''
Given an integer N and a particular digit D, determine the smallest possible integer x that
you can add to N, such that the resulting value does not contain the digit D.
Input:
The first line of the Input contains one integer T, the number of test independent test
cases
The next T lines contains 2 integer each, N and D
Constraints: 
1<=N<=10^9
0<=D<=9
Output:
Output T space separated integers in a single line, the i th integer being the answer to the
i th query
Example:
Input:
2
50 1
92 9
Output:
2 8 '''

def smallest_integer(N,D):
    N_str=str(N)
    D_str=str(D)

    for i in range(N,N+10):
        if D_str not in str(i):
            return abs(N-i)
#input
T=int(input("Enter the number of Test cases : "))
result1=[]
for _ in range(T):
    N,D=map(int,input("Enter the positive integers and the digit separated by a space: " ).split())
    result=smallest_integer(N,D)
    result1.append(result)
print("The smallest possible integer that you can add to the given number respectively are : ")
for j in result1:
    print(j,end=" ")
    
    

    
