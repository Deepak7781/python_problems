'''
To find the mean of the elements of the array. 

Mean = (Sum of elements of the Array) /
       (Total no of elements in Array)

Examples: 

Input : 1 2 3 4 5
Output : 3

Input : 1 2 3
Output : 2

To find the mean using recursion assume that the problem is already solved for N-1 ie you have to find for n

Sum of first N-1 elements = (Mean of N-1 elements)*(N-1)

Mean of N elements = (Sum of first N-1 elements + N-th elements) / (N)

Note : Since array indexing starts from 0, we access N-th element using A[N-1].

'''



def findMean(arr,n):
    if n==1:
        return arr[n-1]
    else:
        return ((findMean(arr,n-1)*(n-1)+arr[n-1])/n)

arr = [1,2,3,4,5]
n = len(arr)
print(findMean(arr,n))