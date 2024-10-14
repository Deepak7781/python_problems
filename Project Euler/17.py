dig = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9': 'Nine','100':'Hundred','1000':'Thousand'}

#tens = {'1':'Ten', '2':'Twenty', '3':'Thirty', '4':'Fourty', '5':'Fifty', '6':'Seventy','7':'Seventy', '8':'Eighty', '9':'Ninty'}

sp_tens = {'10':'Ten', '20':'Twenty', '30':'Thirty', '40':'Fourty', '50':'Fifty', '60':'Sixty','70':'Seventy', '80':'Eighty', '90':'Ninty'}
#num = int(input("Enter the number :"))

def splitUp(num):
    digits = []
    str_num = str(num)
    if str_num[-1] != '0':
        i = 0
        while num:
            rem = num % 10
            digits.append(rem * (10 ** i))
            num = num//10
            i += 1
    elif str_num in sp_tens:
        digits.append(num)
    digits.reverse()
    return digits

def splitUp_sp(num):
    digits = []
    str_num = str(num)
    rem = 1
    while rem != 0:
        number = str(num)
        length = len(number)
        if len(number) > 2:
            digit = num // 10**(length - 1)
            digits.append(digit)
            digits.append(10**(length-1))
        else:
            digits.append(num)
        num = num % 10**(length - 1)
        rem = num % 10**(length - 1)
    return digits
'''
def num_to_words(num):
    words = ''
    num_ = str(num)
    length = len(num_)

    temp = num
    digits = []
    c_digits = []
    if str(temp) not in sp_tens and str(temp)[-1::] not in '0':
        i = 0
        while temp:
            rem = temp % 10
            digits.append(rem * (10 ** i))
            temp = temp//10
            i += 1

        digits.reverse()
    
    else:
        digits.append(num)

    for number in digits:
        numb = str(number)
        if (len(numb) > 2) :
            first = int(numb[0])
            number_ = int(numb)
            c_digits.append(first)
            c_digits.append(number_//first)
        else:
            c_digits.append(int(numb))


    for n in c_digits:
        n_ = str(n)
        if len(n_) == 2:
            words += sp_tens[n_] + ' '
        elif n_ == '100' and len(n_) > 3:
            words += dig[n_] +  ' and '
        else:
            words += dig[n_] + ' '

    return words

print(num_to_words(num))

sum_ = 0
for i in range(1,1001):
    w = num_to_words(i)
    w.replace(" ","")
    sum_ += len(w)
    print(sum_)

'''
num = int(input("Enter number :"))
if str(num)[-1] == '0':
    print(splitUp_sp(num))
else:
    print(splitUp(num))