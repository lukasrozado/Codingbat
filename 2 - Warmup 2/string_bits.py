def string_bits(str1):
    result = ""
    for letters in range(len(str1)):
        if letters % 2 == 0:
            result = result + str1[letters]
    return result