#Check divisibility by 7 without using modulo operator

def div_by_7(num):

    if num<0:
        return div_by_7(-num)
    if num==0 or num==7:
        return True
    if num<10:
        return False

    return div_by_7( num // 10 - 2 * ( num - num // 10 * 10 ) )

num=int(input("Enter a positive integer :"))

if(div_by_7(num)):
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")



'''Divisibility by 7 can be checked by arecursive method. A number of form 10a+b is divisible by 7 if and if a-2b is divisible nby 7

In words, subtract twive the last digit from the number formed by the remaining digits'''

