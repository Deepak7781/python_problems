def div_by_13(num):
    length=len(num)

    if(length==1 and num[0]!='0'):
        return False

    if(length%3==0):
        return int(num)%13==0
    

    if(length%3==1):
        num=str(num)+"00"
        length+=2

    

    elif(length%3==2):
        num=str(num)+"0"
        length+=1

    sum=0
    p=1

    for i in range(length-1,-1,-1):
        group=0

        group+=ord(num[i])-ord('0')
        i-=1
        group+=(ord(num[i])-ord('0'))*10
        i-=1
        group+=(ord(num[i])-ord('0'))*100

        sum=sum+group*p

        p*=(-1)
        
    sum=abs(sum)

    return(sum%13==0)

if __name__=="__main__":
    number=input("Enter a positive integer :")
    if(div_by_13(number)):
        print(number,"is divisible by 13")
    else:
        print(number,"is not divisible by 13")


#The Logic


'''
1. A number is divisible by 13 if and only if the alternating sum (alternatively adding and subtracting) of blocks of three from right to left is divisible by 13. For example, 2911285
is divisible by 13 because the alternating sum of blocks of size 3 is 2-911+285 = -650 which is divisible by 13

2.A number is divisible by 13 if and only if the number obtained by adding the last digit multiplied by 4 to the rest is also divisible by 13

For example, Consider 2353. Applying above rule, we get 235 + 4*3 =247. Again we apply the rule and get 24+7*4 =52.
Since 52 is divisible by 13, the given number is divisible by 13.'''

#The reason behind using ord()

'''In the provided code, the ord function is used to convert individual characters from the string representation of digits to their corresponding integer values.
The ord function returns the Unicode code point of a character. Since the digits '0' to '9' have consecutive Unicode code points, subtracting the code point of '0' from the code point
of a digit gives the integer value of that digit.

Using int could be an alternative approach, but it would be less concise in this context. The int function is typically used to convert a whole string (representing an integer)
to an integer, but here, the goal is to convert individual characters. The use of ord is a concise way to achieve this specific conversion for individual digits.'''

    
