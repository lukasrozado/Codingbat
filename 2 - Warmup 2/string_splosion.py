#Given a non-empty string like "Code" return a string like "CCoCodCode".
#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

def string_splosion(str1):
    result = ""
    for letters in range(len(str1)):
        result = result + str1[:letters+1]
    return result
