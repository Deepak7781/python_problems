n=int(input("Enter a number :"))
x=int(input("Enter first divisor :"))
y=int(input("Enter second divisor :"))
sum=0
j=[]
list=[]
for i in range(1,n+2):
    list.append(i)
    if(i%x==0 and i%y==0):
        j.append(i)
print(list)
print(j)
for k in j:
    list[k]=n
    list[n]=k
    n=n-1
    sum+=list[k]       

print(sum)
print(list)



    

