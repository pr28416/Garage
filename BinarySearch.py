# Binary search function
def binarySearch(element, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if element == lst[mid]:
            return mid
        elif element < lst[mid]:
            up = mid
        else:
            lo = mid + 1
    return None


# Test the code
numbers = [2, 8, 9, 11, 12, 26, 27, 29, 33, 36, 37, 42, 44, 46, 47, 52, 56, 57, 58, 60, 61, 64, 68, 70, 72, 73, 76, 77, 78, 80, 82, 83, 95, 96, 98, 99]
# print("Index of 68:", binarySearch(68, numbers))

sequence = [i for i in range(1, 10**7+1)]
print("Start now")
item = 9999995
i = 0
while sequence[i] != item:
    i += 1
# i = binarySearch(item, sequence)
print("Found at index:", i)
