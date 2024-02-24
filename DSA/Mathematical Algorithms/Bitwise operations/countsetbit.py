#Count the number of set bit
#Write a program to efficiently count the number of 1's in binary representation of an integer
'''
def countSetBit(n):
    count=0
    while(n):
        count+=n&1
        n>>=1
    return count

i=int(input("Enter a number : "))
print("The number of set bits :",countSetBit(i))

'''
#method 2 :using Brian Kernighan's Algorithm

'''
Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit. 
for example : 
10 in binary is 00001010 
9 in binary is 00001001 
8 in binary is 00001000 
7 in binary is 00000111 
So if we subtract a number by 1 and do it bitwise & with itself (n & (n-1)), we unset the rightmost set bit. If we do n & (n-1) in a loop and count the number of times the loop executes, we get the set bit count. 
The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer. 

'''

'''
Algorithm for method 2

1.initialize count=0
2.if integer n is not zero
    a) do bitwise & with (n-1) and assign value back to n
    b)Increment count by 1
    c)go to step 2
3.Else return count
'''

def countsetbits(n):
    count=0
    while(n):
        n &= n-1
        count+=1
    return count

number=int(input("Enter a positive number :"))
print("The number of set bits :",countsetbits(number))