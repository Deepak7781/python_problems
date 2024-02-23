#CHECK IF A GIVEN LARGE NUMBER IS DIVISIBLE BY 3

'''Given a number, the task is that we divide number by 3.
The input number may be large and it may not be possible to store even if we use long long int.'''


def div_by_3(n):
    digit_sum=0
    while n>0:
        rem=n%10
        digit_sum+=rem
        n=n//10

    return(digit_sum%3==0)


n=int(input("Enter a positive integer :"))
if(div_by_3(n)):
    print("Yes the number is divisible by 3")
else:
    print("No, the number is  not divisible by 3")



        
'''Since input number may be very large, we cannot use n % 4 to check if a number is divisible by 4 or not, especially in languages like C/C++. The idea is based on following fact.'''

'''The logic behind this code is that when we add the individual digits of a number and the sum of these digits are divided by 3, then the whole number is divisible by 3'''

'''Let us consider 1332, we can write it as
1332 = 1*1000 + 3*100 + 3*10 + 2
The proof is based on below observation:
Remainder of 10i divided by 3 is 1
So powers of 10 only result in value 1.
Remainder of "1*1000 + 3*100 + 3*10 + 2"
divided by 3 can be written as : 
1*1 + 3*1 + 3*1 + 2 = 9
The above expression is basically sum of
all digits.
Since 9 is divisible by 3, answer is yes.'''
