
def find_num(hcf,lcm,a):
    return hcf*lcm//a

hcf=int(input("Enter the Highest Common Factor :"))
lcm=int(input("Enter the Least Common Multiple :"))
a=int(input("Enter one of the number: "))
print("The other number is",find_num(hcf,lcm,a))
    
