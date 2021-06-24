

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


def rangeSums(lst, queries):
    # Generate prefix sum array - Add an extra 0 at the
    # front to avoid out-of-bound index errors
    sums = [0] * (len(lst)+1)
    for i in range(len(lst)):
        sums[i+1] = sums[i] + lst[i]
    # Solve each query, return list of answers
    answers = [0] * len(queries)
    for q, query in enumerate(queries):
        answers[q] = sums[query[1]+1] - sums[query[0]]
    return answers

# Test code
rs = rangeSums([2, 11, 5, 3, 6, 8], [(2, 3), (0, 4), (3, 5)])
for ans in rs: print(ans)



# lst = [1, 3, 5, 7, 9, 11]
# print(binarySearch(1, lst))
# print(binarySearch(3, lst))
# print(binarySearch(5, lst))
# print(binarySearch(7, lst))
# print(binarySearch(9, lst))
# print(binarySearch(11, lst))
# print(binarySearch(0, lst))
# print(binarySearch(12, lst))