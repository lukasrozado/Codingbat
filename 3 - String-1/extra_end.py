#Given a string, return a new string made of 3 copies of the last 2 chars of 
# the original string. The string length will be at least 2.


#extra_end('Hello') → 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'

def extra_end(str1):
    length = len(str1)
    #REMOVE TWO LETTERS OF THE FIRST ONES AND THEN IMPROVE FROM THE ORINAL LENGHT
    return str1[length - 2 : length] * 3
