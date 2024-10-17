def insertion(lst):
    n = len(lst)
    for i in range(1,n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

print(insertion([5,3,2,6,1]))

#time complexity : O(n^2)
#space complexity : O(1)

