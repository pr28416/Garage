

def numToList(integer):
    digits = []
    while integer > 0:
        digits.insert(0, integer % 10)
        integer //= 10
    return digits


def binarySearch(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x == mid: return mid
        elif x < mid: up = mid
        else: lo = mid + 1



print()