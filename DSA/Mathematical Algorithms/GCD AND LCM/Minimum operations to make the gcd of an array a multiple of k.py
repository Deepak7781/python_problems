#Minimum operations to make GCD of array a multiple of k

#Problem
'''
Given an array and k, we need to find the minimum operations needed to make GCD of the array equal or multiple of k.
Here an operation means either increment or decrements an array element by 1.

Examples:

Input : a = { 4, 5, 6 }, k = 5 
Output : 2 
Explanation : We can increase 4 by 1 so that it becomes 5 and decrease 6 by 1 so that it becomes 5. Hence minimum operation will be 2.

Input : a = { 4, 9, 6 }, k = 5 
Output : 3 
Explanation : Just like the previous example we can increase and decrease 4 and 6 by 1 and increase 9 by 1 so that it becomes 10. Now each element has GCD 5.
Hence minimum operation will be 3.
'''

#Logic
'''
Here we have to make the gcd of the array equal or multiple to k, which means there will be cases in which some elements are near k or to some of its multiple. So, to solve this we just
have to make each array value equal to or multiple to K. By doing this we will achieve our solution as if every element is multiple of k then it’s GCD will be at least K.
Now our next target is to convert the array elements in the minimum operation i.e. minimum number of increment and decrement. This minimum value of incrementor decrement can be known
only by taking the remainder of each number from K i.e. either we have to take the remainder value or (k-remainder) value, whichever is minimum among them.

'''

def minOperation(arr,length,k):
    result =0
    for i in range(n):
        if(arr[i]!=1 and arr[i]>k):
            result=(result+min(arr[i]%k,k-arr[i]%k))
        else:
            result=result+k-arr[i]
    return result

a=list(map(int, input("Enter the numbers separated by comma :").split(',')))
n=len(a)
k_=int(input("Enter the multiple value :"))
print(minOperation(a,n,k_))
