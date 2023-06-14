https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    renum = str(num)
    result = ""
    for i in renum:
        result = result + str(int(i)**2)
    return int(result)