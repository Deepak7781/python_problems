#Time complexity : O(n)
#Space complexity : O(1)


def sentinalsearch(arr,n,key):
    last = arr[n-1]

    arr[n-1] = key
    i = 0
    while arr[i]!=key:
        i+=1
    arr[n-1] = last
    if (i<n-1) or (arr[n-1] == key):
        print("Element is present at index",i)
    else:
        print("Element is not present")

arr = [3,6,3,44,77,43]
key = 88

sentinalsearch(arr,len(arr),key)