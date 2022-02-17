def longestUniqueSubstring(string):
    if len(string) == 0: return 0
    lo, up, maxBounds = 0, 1, (0, 1)
    used = {string[lo]}
    while up < len(string):
        if string[up] in used:
            used.remove(string[lo])
            lo += 1
        else:
            used.add(string[up])
            up += 1
        if up - lo > maxBounds[1] - maxBounds[0]:
            maxBounds = (lo, up)
    return maxBounds[1] - maxBounds[0]

print(longestUniqueSubstring("abacdabcca"))