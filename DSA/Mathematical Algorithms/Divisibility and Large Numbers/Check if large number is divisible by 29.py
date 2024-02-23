def div_by_29(n):
    while(int(n/100)):
        last_digit=int(n%10)
        n=int(n/10)
        n+=last_digit*3
    return n%29==0

n=int(input("Enter a positive integer :"))
if(div_by_29(n)):
    print(n ,"is divisible by 29")
else:
    print(n, "is not divisible by 29")

#THE LOGIC

'''
To check if a number is divisible by 29 or not to add 3 times of last digit to rest number and repeat this process until number comes 2 digit.
Example:

Number 348

Three times of last digit + Rest of the number = 8*3 +34 =58

Since 58 is divisible by 29 so 348 is also divisible by 29
'''
