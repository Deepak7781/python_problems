#Given a positive integer n, calculate the sum of the absolute difference between each pair of adjacent digits.
'''Example
Input
1524

Output
9

Explanation
The number 1524, the absolute differences are:
|5-1| = 4
|2-5| = 3
|4-2| = 2

Total sum: 4 + 3 + 2 = 9'''

input_number=int(input("Enter a number :"))
single_digit=[]
absolutedifference=0

sum=0
if(1<=input_number<=10000):
    while(input_number!=0):
        k=input_number%10
        single_digit.append(k)
        input_number=int(input_number/10)
    for i in range(len(single_digit)-1,0,-1):
            absolutedifference=abs(single_digit[i]-single_digit[i-1])
            sum+=absolutedifference
    print(sum)