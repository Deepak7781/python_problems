
n = int(input("Enter the number :"))

sum_of_first = (n*(n+1))/2

sum_of_square_of_first = (n*(n+1)*((2*n)+1))/6

diff = ((sum_of_first)**2) - sum_of_square_of_first 

print(int(diff))