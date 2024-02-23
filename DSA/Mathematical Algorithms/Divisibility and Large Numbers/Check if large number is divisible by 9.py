

def div_by_9(n):
    digit_sum=0
    while n>0:
        rem=n%10
        digit_sum+=rem
        n=n//10

    return digit_sum%9==0

num=int(input("Enter a positive integer :"))
if(div_by_9(num)):
    print("The number is divisible by 9")
else:
    print("The number is not divisible by 9")


''' A number is divisible by 9 iif sum of its digits ids divisible by 9'''
