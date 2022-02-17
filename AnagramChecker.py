def checkAnagram(s1, s2):
    chars = {}
    for c in s1:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c in s2:
        if c in chars:
            chars[c] -= 1
            if chars[c] < 0:
                return False
        else:
            return False
    for c in chars:
        if chars[c] != 0:
            return False
    return True

print(checkAnagram('ratatouille', 'leruiatlaot'))