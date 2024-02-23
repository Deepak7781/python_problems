

def div_by_4(st):

    n=len(st)
    if(n==0):
        return False
    if(n==1):
        return((st[0])-'0'%4==0)

    last_digit=int(st[n-1])
    second_last_digit=int(st[n-2])
    return(second_last_digit*10 + last_digit %4 ==0)

st=input("Enter a positive integer :")

if(div_by_4(st)):
    print("Yes, the number is divisible by 4")
else:
    print("No, the number is not divisible by 4")


'''Since input number may be very large, we cannot use n % 4 to check if a number is divisible by 4 or not, especially in languages like C/C++. The idea is based on following fact.

A number is divisible by 4 if number formed by last two digits of it is divisible by 4.'''


'''Let us consider 76952, we can write it as
76952 = 7*10000 + 6*1000 + 9*100 + 5*10 + 2

The proof is based on below observation:
Remainder of 10i divided by 4 is 0 if i greater 
than or equal to two. Note than 100, 1000,
... etc lead to remainder 0 when divided by 4.

So remainder of "7*10000 + 6*1000 + 9*100 + 
5*10 + 2" divided by 4 is equivalent to remainder 
of following : 
0 + 0 + 0 + 5*10 + 2 = 52
Therefore we can say that the whole number is 
divisible by 4 if 52 is divisible by 4.'''
