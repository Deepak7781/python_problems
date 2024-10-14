"""If we list all the natural numbers below 10 that are multiples of 3 and 5
    ,we get 3,5,6 and 9. The sum of these multiples is 23.
    
    Find the sum of all the multiples of 3 or 5 below 1000"""
'''
sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
'''

def sum_of_multiples(x,n):
    p = (n-1)//x
    return x*(p*(p+1) // 2)

n = int(input("Enter the the end term :"))
summation = sum_of_multiples(3,n) + sum_of_multiples(5,n) - sum_of_multiples(15,n)
print(summation)
print(sum_of_multiples(2,100))