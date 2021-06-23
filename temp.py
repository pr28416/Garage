

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
        if x == lst[mid]: return mid
        elif x < lst[mid]: up = mid
        else: lo = mid + 1


lst = [1, 3, 5, 7, 9, 11]
# print(binarySearch(1, lst))
# print(binarySearch(3, lst))
# print(binarySearch(5, lst))
# print(binarySearch(7, lst))
# print(binarySearch(9, lst))
# print(binarySearch(11, lst))
# print(binarySearch(0, lst))
# print(binarySearch(12, lst))