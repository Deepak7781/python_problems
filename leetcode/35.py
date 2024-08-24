def searchPosition(nums,target):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return low

num = [1,3,5,7]
target = 9

print(searchPosition(num,target))