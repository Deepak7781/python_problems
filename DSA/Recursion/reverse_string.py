
def reverse_string(s,rev = ""):
    if len(s) == 0:
        return rev
    else:
        rev = rev + s[-1]
        return reverse_string(s[:-1],rev)
    

print(reverse_string("pots&pans"))