https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for i in sentence:
        if i in vowels:
            result +=1
    return result