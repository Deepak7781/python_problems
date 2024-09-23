def string_to_int(s):
    if len(s) == 0:
        return 0
    first_digit = ord(s[0]) - ord('0')
    rest_of_string = string_to_int(s[1:])

    return first_digit*(10**(len(s)-1)) + rest_of_string

print(string_to_int('12345'))

