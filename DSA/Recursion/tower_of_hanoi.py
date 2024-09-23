def towersOfHanoi(disks, start, end):
    if disks == 1:
        print(f'{disks} : {start} -> {end}')
    else:
        other = 6 - (start + end)
        towersOfHanoi(disks-1,start,other)
        print(f'{disks} : {start} -> {end}')
        towersOfHanoi(disks-1, other, end)

towersOfHanoi(3,1,3)

