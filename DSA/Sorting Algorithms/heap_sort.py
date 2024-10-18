def heapify(nums,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i+ 2
    if left < n and nums[left] > nums[largest]:
        largest = left

    
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums,n, largest)

def create_heap(nums):
    for i in range(len(nums)//2 -1 ,-1, -1):
        heapify(nums,len(nums),i)
    return nums

def heap_sort(heap):
    n = len(heap)
    create_heap(heap)
    for i in range(n-1,0,-1):
        heap[0],heap[i] = heap[i],heap[0]
        heapify(heap,i,0)
    return heap


heap = [10,20,15,30,40]
print(heap_sort(heap))

