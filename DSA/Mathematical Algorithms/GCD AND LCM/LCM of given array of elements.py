#To find the lcm of array of elements

def get_lcm(num1, num2):
    if(num1>num2):
	    num = num1
	    den = num2
    else:
        num=num2
        den=num1
    rem=num%den
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    gcd=den
    lcm=int(int(num1*num2)/int(gcd))
    return lcm

l=list(map(int, input("Enter the numbers separated by commas :").split(',')))

num1=l[0]
num2=l[1]
lcm=get_lcm(num1,num2)

for i in range(2,len(l)):
    lcm=get_lcm(lcm,l[i])

print("The LCM is",lcm)
