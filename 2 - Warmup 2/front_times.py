#Given a string and a non-negative int n, we'll say that the front of the 
# string is the first 3 chars, or whatever is there if the string is less 
# than length 3. Return n copies of the front;


#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str1, n):
    if len(str1) >= 3:
        return str1[0:3]*n
    else:
        return str1[0:]*n
