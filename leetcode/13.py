#method1
'''
def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    number = 0

    for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    return number

'''
def romanToInt(roman):
    roman_ = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman = roman.replace('IV','IIII').replace('IX','VIIII')
    roman = roman.replace('XL','XXXX').replace('XC','LXXXX')
    roman = roman.replace('CD','CCCC').replace('CM','DCCCC')
    total = 0
    for r in roman:
        total += roman_[r]
    return total
s = "MCMXCIV"
print(romanToInt(s))


'''
#using basics
def romanToInt(s):
        sum=0
        for i in range(len(s)):
            if(i<len(s)-1):
                if(s[i]=='I'and s[i+1]=='V'):
                    sum+=4
                    continue
                if(s[i]=='I'and s[i+1]=='X'):
                    sum+=9
                    continue
                if(s[i]=='X'and s[i+1]=='L'):
                    sum+=40
                    continue
                if(s[i]=='X'and s[i+1]=='C'):
                    sum+=90
                    continue
                if(s[i]=='C'and s[i+1]=='D'):
                    sum+=400
                    continue
                if(s[i]=='C'and s[i+1]=='M'):
                    sum+=900
                    continue
            if(i==0):
                if(s[i]=='I'):
                    sum+=1
                if(s[i]=='V'):
                    sum+=5
                if(s[i]=='X'):
                    sum+=10
                if(s[i]=='L'):
                    sum+=50
                if(s[i]=='C'):
                    sum+=100
                if(s[i]=='D'):
                    sum+=500
                if(s[i]=='M'):
                    sum+=1000
            if(i>=1):
                if(s[i]=='I'):
                    sum+=1   
                if(s[i]=='V'and s[i-1]!='I'):
                    sum+=5
                if(s[i]=='X' and s[i-1]!='I'):
                    sum+=10
                if(s[i]=='L' and s[i-1]!='X'):
                    sum+=50
                if(s[i]=='C' and s[i-1]!='X'):
                    sum+=100
                if(s[i]=='D' and s[i-1]!='C'):
                    sum+=500
                if(s[i]=='M' and s[i-1]!='C'):
                    sum+=1000    
            
        return sum
        
n=input("Enter the roman integer :")
print(romanToInt(n))
 
'''