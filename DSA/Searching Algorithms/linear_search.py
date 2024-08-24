#Time complexity : O(n)
#space complexity : O(1)

def linear_search(arr,T):
    for i in range(len(arr)):
        if arr[i] == T:
            return i
    return -1

arr = [1,2,3,4,5,6,7,8,9]
T= 10
if linear_search(arr,T) == -1:
    print("Element is not present in the array")
else:
    print(f"Element is present in index position {linear_search(arr,T)}")
