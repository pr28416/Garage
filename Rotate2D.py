def rotate(array):
    R, C = len(array), len(array[0])
    newArr = [[None] * R for _ in range(C)]
    for c in range(C):
        for r in range(R-1, -1, -1):
            newArr[C-c-1][r] = array[r][c]
    return newArr

i = rotate([
[1 ,  2 ,  3 ,  4 ,  5],
[6 ,  7 ,  8 ,  9 ,  10],
[11,  12,  13,  14,  15],
# [16,  17,  18,  19,  20],
# [21,  22,  23,  24,  25]
])
for j in i:
    print(*j)

'''
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25

5   10  15  20  25
4   9   14  19  24
3   8   13  18  23
2   7   12  17  22
1   6   11  16  21

'''