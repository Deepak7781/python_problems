def addBinary(num1, num2):
    sum = []
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        if i >=0:
            carry += int(num1[i])
            i -= 1
        if j >= 0:
            carry += int(num2[j])
            j -= 1
        
        sum.append(str(carry % 2))
        carry //= 2

    return ''.join(reversed(sum))
    
num1 = "101001"
num2 = "0101"
print(addBinary(num1,num2))