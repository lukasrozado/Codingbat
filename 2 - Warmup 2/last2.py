#Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).

#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2


def last2(str1): 
    #SET THE COUNTERS AND LOCK THE NUMBERS IN THE STRING
    if len(str1) < 2:
        return 0
    last2 = str1[len(str1)-2:]
    count = 0
    for every in range(len(str1)-2):
        result = str1[every:every+2]
        if result == last2:
            count += 1
    return count

