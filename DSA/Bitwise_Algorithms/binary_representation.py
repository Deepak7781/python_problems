#Representing a decimal number in bianry system

#method 1: Iterative
'''def bin(n):
    i=1<<15
    while i>0:

        if((n&i) !=0):
            print("1",end="")
        else:
            print("0",end="")
        i=i//2
n=int(input("Enter any number :"))
bin(n)'''

#method 2 :Recursive

'''def bin(n):

    if n>1:
        bin(n//2)
    print(n%2,end="")

bin(7)'''

#method 3 :using inbuilt library
def binary(n):
    return(int(bin(n).split('0b')[1]))

x=int(input("Enter a number : "))
print("The binary number is ",binary(x))