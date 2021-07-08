# Manacher's algorithm

def longestPalindrome(string):
    modified = [string[i//2] if i % 2 == 1 else None for i in range(len(string)*2+1)]
    # modified = string
    counts = [1] * len(modified)
    center = 0
    while center < len(modified):
        # Expand new center
        lo, up = center-((counts[center]-1)//2), center+((counts[center]-1)//2)
        while lo >= 0 and up < len(modified):
            if modified[lo] != modified[up]:
                break
            lo -= 1
            up += 1
        lo += 1
        up -= 1
        counts[center] = up-lo+1
        # Break out if up is at the end
        if up >= len(modified)-1: break
        # Look for new center
        centerLooker = center+1
        while centerLooker <= up:
            mirrored = center-(centerLooker-center)
            if (counts[mirrored]-1)//2 > up-centerLooker: # No space to expand
                # print('no space to expand at', centerLooker)
                counts[centerLooker] = (up-centerLooker)*2+1
                centerLooker += 1
            elif (counts[mirrored]-1)//2 < up-centerLooker: # Too little space
                # print('too little space to expand at', centerLooker)
                counts[centerLooker] = counts[mirrored]
                centerLooker += 1
            else: # Found center
                # print('found center')
                counts[centerLooker] = counts[mirrored]
                break
        center = centerLooker
        # print('new center:', center, counts[center], lo, up)
    longestIdx = 0
    print(counts)
    for i in range(len(counts)):
        if counts[i] > counts[longestIdx]:
            longestIdx = i
    return "".join(filter(lambda c: c != None, modified[longestIdx-(counts[longestIdx]-1)//2:longestIdx+(counts[longestIdx]-1)//2+1]))

print(longestPalindrome(input()))