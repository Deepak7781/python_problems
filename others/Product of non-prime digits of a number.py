input_number=int(input("Enter a number :"))
primes=[2,3,5,7]
product=1
flag=False
if(input_number==0):
    product=1
while(input_number!=0):
    single_digit=input_number%10
    if(single_digit not in primes):
        flag=True
        product*=single_digit
    input_number=int(input_number/10)
if(flag==False):
    product=1
print(product)
