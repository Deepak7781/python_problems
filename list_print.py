lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  
print("The list you entered is :",lst)
for j in lst:
    if(j<5):
        print(j)
