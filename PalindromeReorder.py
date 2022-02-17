def makePalindrome(string):
    chars = [[chr(65+i), 0] for i in range(26)]
    for c in string:
        chars[ord(c)-65][1] += 1
    chars = list(filter(lambda x: x[1] != 0, chars))
    mid_idx = None
    for i in range(len(chars)-1, -1, -1):
        if chars[i][1] % 2 == 1:
            if mid_idx is not None:
                return "NO SOLUTION"
            mid_idx = i
    if mid_idx == None: mid_idx = 0
    middle = chars[mid_idx][0] * chars[mid_idx][1]
    tail = ""
    for i in range(len(chars)):
        if i == mid_idx: continue
        tail += chars[i][0] * (chars[i][1]//2)
    return tail + middle + tail[::-1]