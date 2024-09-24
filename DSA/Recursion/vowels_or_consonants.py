def vowels_or_consonants(s, vowels = 0, consonants = 0, index = 0):
    if index == len(s):
        return vowels > consonants
    
    char = s[index].lower()

    if char in 'aeiou':
        vowels += 1
    else:
        consonants += 1
    
    return vowels_or_consonants(s, vowels, consonants, index+1)

string = input("Enter your string :")

if vowels_or_consonants(string):
    print("Your string has more vowels than consonants")
else:
    print("Your string has more consonants than vowels")