#Minimum squares to cut a rectangle evenly
'''
Given a rectangular sheet of length l and width w. we need to divide this sheet into square sheets such that the number of square sheets should be as minimum as possible.
Examples:
 

Input :l= 4 w=6 
Output :6 
We can form squares with side of 1 unit, But the number of squares will be 24, this is not minimum. If we make square with side of 2, then we have 6 squares. and this is our required answer. 
And also we can’t make square with side 3, if we select 3 as square side, then whole sheet can’t be converted into squares of equal length.
'''
#Logic
'''optimal length of the side of a square id equal to GCD of two numbers'''

from math import gcd

def minsquare(l,b):
    length=gcd(l,b)
    return int((l*b)/(length*length))

l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the rectangle :"))
print(minsquare(l,b))
