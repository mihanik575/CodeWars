https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    list_num = numbers.split()
    list_num = [int(i) for i in list_num]
    return str(max(list_num)) + " " + str(min(list_num))