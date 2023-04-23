# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399

def quadrant(x, y):
    quadrant = 0
    if x > 0 and y > 0:
        quadrant = 1
    if x > 0 and y < 0:
        quadrant = 4
    if x < 0 and y > 0:
        quadrant = 2
    if x < 0 and y < 0:
        quadrant = 3
    return quadrant

print(quadrant(1, 3))