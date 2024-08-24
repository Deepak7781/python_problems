'''
In algebra, Discriminant helps us deduce various properties of the roots of a polynomial or polynomial function without even computing them. 
Let’s look at this general quadratic polynomial of degree two: 
 

ax^2+bx+c

Here the discriminant of the equation is calculated using the formula: 
 

b^2-4ac 

Now we can deduce the following properties: 
 

    If the discriminant is equal to zero then the polynomial has equal roots i.e., a=b.
    If the discriminant is positive and the coefficients are real, then the polynomial has two real roots.

Here are a few conditions that we must keep in mind while programming and making deductions from the discriminant: 
 

    If the discriminant is equal to zero then one solution is possible.
    If the discriminant is positive then two solutions are possible.
    If the discriminant is negative then no real solutions are possible.

Examples: 
 

Input:
a = 20
b = 30
c = 10
Explanation:
(30**2) - (4*20*10) 
Output:
Discriminant is 100 which is positive
Hence Two solutions

Input:
a = 9
b = 7
c = 12
Explanation:
(30**2) - (4*20*10) 
Output:
Discriminant is -383 which is negative
Hence no real solutions


'''


def discriminant(a,b,c):
    return (b**2)-(4*a*c)

a,b,c = map(int, input("Enter the values of a,b,c :").split())
dis = discriminant(a,b,c)
print(f"Discriminant = {dis}")
if dis == 0:
    print("Roots are equal")
elif dis > 0 :
    print("The roots are real")
else:
    print("No real roots")