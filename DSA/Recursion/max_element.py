def max_element(lst,maximum):
    if len(lst) == 0:
        return maximum
    else:
        if maximum < lst[0]:
            maximum = lst[0]
        return max_element(lst[1:],maximum)

print(max_element([1,2,7,5],0))
    