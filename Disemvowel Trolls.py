https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for i in range(len(string_)):
        if string_[i] not in vowels:
            result = result + string_[i]
    return result