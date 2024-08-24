#converting the integer to string

def palindrome(s):
    num=str(s)
    return num[::-1]==num
print(palindrome(121))


#without converting to a string

def palin(x):
    num=0
    temp=x
    while temp:
        rem=temp%10
        num=(num*10)+rem
        temp=temp//10
    return num==x 
print(palin(1212))
    
