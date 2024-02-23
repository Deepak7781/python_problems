
def div_by_6(st):

    n=len(st)

    if(int(st[n-1]))%2 !=0 :
       return False

    digit_sum=0
    for i in range(0,n):
        digit_sum+=int(st[i])

    return(digit_sum%3==0)

st=input("Enter a positive integer")

if(div_by_6(st)):
    print("The given number is divisible by 6")
else:
    print("The given number is not divisible by 6")


''' The logic behind the code is that if a number is divisible by 6 the n the number is divisible by 2 and 3 so we check if the number is divisibke by two amd then use the logic which
we used for divisibility check for 3'''

