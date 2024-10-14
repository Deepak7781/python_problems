'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2
, the first terms will be:
    1,2,3,5,8,13,21,34,55,89,......
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''


def fib(n):
    dp = [0,1]
    for i in range(2,n+1):
        new = dp[i-2] + dp[i-1]
        dp.append(new)
    return dp[n]

n = 0
sum = 0 

while fib(n) < 4000000:
    if fib(n) % 2 == 0:
        sum += fib(n)
    n += 1

print(sum)


''' 
Hacker Rank Accepted solution

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        summation = 0
        first = 0
        second = 1
        fibonacci = [first,second]
        while True:
            result = first + second
            fibonacci.append(result)
            first,second = second,result
            if result > n:
                break
            if result % 2 == 0:
                summation += result
        print(summation)
                

'''