def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    base = strs[0]
    for i in range(len(strs)):
        for word in strs:
            if i == len(word) or word[i] != base[i]:
                return base[0:i]
    return base

s = ["deepak","deva","devil"]
print(longestCommonPrefix(s))