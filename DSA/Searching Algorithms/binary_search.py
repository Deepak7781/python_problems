#Time Complexity : O(logn)
#Spce Complexity : O(1)
'''
#iterative approach

def binary(arr,T):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid] == T:
            return mid
        elif arr[mid] < T:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2,4,10,37,50,73,86]
T =3

if binary(arr,T) == -1:
    print("Element is not present in the array")
else:
    print(f"Element is present in index position {binary(arr,T)}")

'''

#recursivce approach


def binary(arr,T,low,high):
    if low<=high:
        mid = low+(high-low)//2
        if arr[mid] == T:
            return mid
        elif arr[mid]<T:
            return binary(arr,T,mid+1,high)
        else:
            return binary(arr,T,low,mid-1)
    else:
        return -1
    
arr = [2,4,10,37,50,73,86]
T =2

if binary(arr,T,0,len(arr)-1) == -1:
    print("Element is not present in the array")
else:
    print(f"Element is present in index position {binary(arr,T,0,len(arr)-1)}")

