def lowerbound(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x <= lst[mid]:
            up = mid
        else:
            lo = mid+1
    return lo

def upperbound(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x < lst[mid]:
            up = mid
        else:
            lo = mid+1
    return lo

def bound_search(x, lst, compare):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if compare(x, lst[mid]):
            up = mid
        else:
            lo = mid+1
    return lo

lower = lambda x, elem: x <= elem
upper = lambda x, elem: x < elem

nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 8]