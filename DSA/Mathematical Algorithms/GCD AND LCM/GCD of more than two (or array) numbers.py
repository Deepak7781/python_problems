#To find the gcd of more than two (or array) numbers

def find_gcd(a,b):
    while(b):
        a,b=b,a%b
    return a

l=list(map(int, input("Enter the numbers separated by comma :").split(',')))
num1=l[0]
num2=l[1]
gcd=find_gcd(num1,num2)
for i in range(2,len(l)):
    gcd=find_gcd(gcd,l[i])
                                  
print("The GCD of the array of elements is",gcd)
