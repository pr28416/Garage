def lbsearch(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x <= lst[mid]: up = mid
        else: lo = mid+1
    return lo

def ubsearch(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x < lst[mid]: up = mid
        else: lo = mid+1
    return lo

def bound_search(x, lst, compare):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo + up) // 2
        if compare(x, lst[mid]): up = mid
        else: lo = mid + 1
    return lo

nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6]
lower = lambda x, elem: x <= elem
upper = lambda x, elem: x < elem
bs = bound_search