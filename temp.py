

def numToList(integer):
    digits = []
    while integer > 0:
        digits.insert(0, integer % 10)
        integer //= 10
    return digits


