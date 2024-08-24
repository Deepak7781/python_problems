def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
hay = "nnsadbutsad"
needle = "sad"
print(strStr(hay,needle))