def plusOne(digits):
        length = len(digits)
        last = length - 1
        if digits[last] != 9:
            digits[last] = digits[last] + 1
        else:
            num_str = ''
            for num in digits:
                num_str += str(num)
            number = int(num_str) + 1
            num_og = str(number)
            index = 0
            for num in num_og:
                if index == length:
                     digits.append(int(num))
                else:
                    digits[index] = int(num)
                index += 1
        return digits

print(plusOne([8,9,8,9]))