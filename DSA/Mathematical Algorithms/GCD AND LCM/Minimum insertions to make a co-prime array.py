#Minimum insertations to make a co-prime array

from math import gcd

def print_result(arr,n):
    count=0

    for i in range(1,n):
        if(gcd(arr[i],arr[i-1]!=1)):
            count+=1
    print("The minimum nuber of insertions to make this array a co-prime array is",count)
    print("The co-prime array is as follows:")
    print(arr[0],end=" ")

    for i in range(1,n):
        if(gcd(arr[i],arr[i-1]!=1)):
            print(1,end=" ")
        print(arr[i],end=" ")


A=list(map(int, input("Enter the numbers separated by comma :").split(',')))
n=len(A)
print_result(A,n)
