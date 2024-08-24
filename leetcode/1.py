#O(n^2) Solution 

'''
def find(lst,target):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                return [i,j]

s=[2,7,11,15]
print(find(s,26))
'''
    

#O(n) Solution

def find(lst,target):
    sum={}
    for i in range(len(lst)):
        diff = target-lst[i]
        if diff in sum:
            return [sum[diff],i]
        else:
            sum[lst[i]]=i

s=[2,7,11,15]    
print(find(s,26))
