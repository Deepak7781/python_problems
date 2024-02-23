

def div_by_15(n):
    length=len(n)
    num=int(n)
    if(length<=3):
        return num%15==0
    if(length>=4):
        if(n[length-1] !='0' and n[length-1]!='5'):
            return False
    
    
        digit_sum=0
        while num>0:
            rem=num%10
            digit_sum +=rem
            num=num//10

        return digit_sum %3 ==0

n=input("Enter a positive integer :")
if(div_by_15(n)):
    print(n,"is divisible by 15")
else:
    print(n,"is not divisible by 15")
