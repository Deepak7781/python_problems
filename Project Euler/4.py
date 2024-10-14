
def isPalindrome(n):
    return str(n) == str(n)[::-1]

a = 999
largestPalindrome = 0
palindromes = {}
while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990 #Largest three digit number which can be divisible by 11
        db = 11
    while b>=a:
        if a*b < largestPalindrome:
            break
        if isPalindrome(a*b):
            largestPalindrome = a*b
            palindromes[largestPalindrome] = (a,b)
        b = b - db
    a = a - 1

print(largestPalindrome)
print(palindromes[largestPalindrome])
