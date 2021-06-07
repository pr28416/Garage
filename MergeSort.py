def mergesort(arr, l, r, comp):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left, l, mid, comp)
    mergesort(right, mid, r, comp)
    k, a, b = 0, 0, 0
    while a < len(left) and b < len(right):
        if comp(left[a], right[b]):
            arr[k] = left[a]
            a += 1
        else:
            arr[k] = right[b]
            b += 1
        k += 1
    while a < len(left):
        arr[k] = left[a]
        a += 1
        k += 1
    while b < len(right):
        arr[k] = right[b]
        b += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
mergesort(arr, 0, len(arr), lambda x, y: x < y)
print(arr)