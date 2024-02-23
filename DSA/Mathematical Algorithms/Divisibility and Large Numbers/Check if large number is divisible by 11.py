

def div_by_11(n):
     num=len(n)
     difference=0
     odd_sum=0
     even_sum=0
     if num>=2:
         odd_num=int(n[0:num:2])
         even_num=int(n[1:num:2])
         
         odd_sum=0
         even_sum=0
         while odd_num>0:
             rem=odd_num%10
             odd_sum+=rem
             odd_num=odd_num//10
         while even_num>0:
             rem=even_num%10
             even_sum+=rem
             even_num=even_num//10

         difference=odd_sum-even_sum
         if difference==0 or difference==11:
             return True

         return difference%11 == 0
     if num==1:
         return False

#Another method
'''
n=input("Enter a positive integer:")
if(div_by_11(n)):
    print("Yes")
else:
    print("No")

    
    
def check(st) :
    n = len(st) 
 
    
    oddDigSum = 0
    evenDigSum = 0
    for i in range(0,n) :

        if (i % 2 == 0) :
            oddDigSum = oddDigSum + ((int)(st[i]))
        else:
            evenDigSum = evenDigSum + ((int)(st[i]))
     

    return ((oddDigSum - evenDigSum) % 11 == 0)
 

st = "76945"
if(check(st)) :
    print( "Yes")
else : 
    print("No ")
'''

#The Logic

'''
Since input number may be very large we cannot use n%11 to check if a number is divisible by 11 to check if a number is divisible by 11 or not especially in languages like C/C++

The following logic is used

" A number is divisible by 11 if difference of following two is divisible 11

1.Sum of digit at odd places
2.Sum of digits at even places "
'''
