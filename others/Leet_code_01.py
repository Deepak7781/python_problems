'''Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.'''

def total_amount(n):
    total_sum = 0
    current_day = 1
    amount = 1
    
    for day in range(1, n + 1):
        total_sum += amount
        amount += 1

        # Check if it's Monday (every 7 days)
        if current_day == 7:
            amount = amount - current_day + 1
            current_day = 0

        current_day += 1

    return total_sum
n=20
print(total_amount(n))

#The best solution
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        q, r= divmod(n, 7)
        return 28*q+7*q*(q-1)//2+(2*q+r+1)*r//2'''
