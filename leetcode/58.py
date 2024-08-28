def lengthOfLastWord(sentence):
    length = 0
    i = len(sentence) - 1
    while i>=0 and sentence[i] == ' ':
        i-=1
    while i>=0 and sentence[i] != ' ':
        length += 1
        i -= 1
    return length

print(lengthOfLastWord("   Hello Who is there   "))


#method 2
#a = a.split()
#return len(a[-1])