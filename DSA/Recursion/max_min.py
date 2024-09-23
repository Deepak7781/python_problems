def max_min(lst, index = 0, maximum = None, minimum = None):
    if index == len(lst):
        return maximum,minimum
    else:
        if maximum is None or maximum < lst[index]:
            maximum = lst[index]
        if minimum is None or minimum > lst[index]:
            minimum = lst[index]
        return max_min(lst, index+1, maximum, minimum)

lst = [1,2,3,14,5,9]

print(max_min(lst))
