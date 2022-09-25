def isUnique(s):
    st = set()
    for i in s:
        if i in st:
            return False
        st.add(i)
    return True

def checkPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

def urlify(s, n):
    return "%20".join(s.split(" "))

def palindromePermutation(s):
    mp = {}
    for c in s:
        c = c.lower()
        if not('a' <= c <= 'z'): continue
        if c in mp: mp[c] += 1
        else: mp[c] = 1
    flag = False
    for k in mp:
        if mp[k] % 2:
            if flag: return False
            flag = True
    return True

def oneAway(s1, s2):
    if abs(len(s1)-len(s2)) > 1: return False
    i = j = 0
    didShift = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if didShift: return False
            didShift = True
            if len(s1) > len(s2): j -= 1
            elif len(s1) < len(s2): i -= 1
        i += 1
        j += 1
    return True

def stringCompression(s):
    if len(s) == 0: return s
    arr = [s[0], 1]
    for i in range(1, len(s)):
        if s[i] == s[i-1]: arr[-1] += 1
        else:
            arr[-1] = str(arr[-1])
            arr.append(s[i])
            arr.append(1)
    arr[-1] = str(arr[-1])
    return "".join(arr)

def rotateMatrix(matrix):
    N = len(matrix)
    for topLeft in range(N//2):
        for c in range(topLeft, N-topLeft-1):
            tmp = matrix[topLeft][N-topLeft-c-1]
            matrix[topLeft][N-topLeft-c-1] = matrix[N-topLeft-c-1][N-topLeft-1]
            matrix[N-topLeft-c-1][N-topLeft-1] = matrix[N-topLeft-1][c]
            matrix[N-topLeft-1][c] = matrix[c][topLeft]
            matrix[c][topLeft] = tmp
    return matrix

def printMatrix(matrix):
    for row in matrix: print(*row, sep="\t")


if __name__ == "__main__":
    # print(isUnique("abcdef"))
    # print(isUnique("abcdefe"))
    # print(isUnique("abcdefab"))
    # print(checkPermutation('abc', 'cab'))
    # print(checkPermutation('abc', 'ccc'))
    # print(checkPermutation('abc', 'cca'))
    # print(checkPermutation('abcd', 'cdba'))
    # print(urlify("Mr John Smith", 13))
    # print(palindromePermutation("Tact Coa"))
    # print(palindromePermutation("racecar"))
    # print(oneAway("pale", "ple"))
    # print(oneAway("pales", "pale"))
    # print(oneAway("pale", "bale"))
    # print(oneAway("pale", "bake"))
    # print(stringCompression("aabcccccaaa"))
    # print(stringCompression(""))
    # print(stringCompression("a"))
    # print(stringCompression("aaa"))
    # print(stringCompression("aaab"))
    printMatrix(rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))