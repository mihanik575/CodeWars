# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

