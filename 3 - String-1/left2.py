#Given a string, return a "rotated left 2" version where the first 2 chars are 
# moved to the end. The string length will be at least 2.

#left2('Hello') → 'lloHe'
#left2('java') → 'vaja'
#left2('Hi') → 'Hi'

def left2(str1):
    length = len(str1)
    return str1[2:length] + str1[0:2]