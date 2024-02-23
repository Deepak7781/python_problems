def div_by_12(n):
    num=len(n)
    if num>=3:
        last_digit=int(n[num-1])
        if last_digit%2!=0:
            return False
        second_last_digit=int(n[num-2])

        digit_sum=0
        for i in range(0,num):
            digit_sum+=int(n[i])
        return digit_sum%3==0 and second_last_digit + last_digit %4 !=0
    else:
        num1=int(n)
        return(num1%12==0)

n=input("Enter a positive integer :")
if (div_by_12(n)):
    print("Yes")
else:
    print("No")
