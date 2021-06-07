def aoi(a, b, c, d):
    x, y = 0, 1
    width = min(b[x], d[x]) - max(a[x], c[x])
    height = min(b[y], d[y]) - max(a[y], c[y])
    if min(width, height) > 0: return width * height
    else: return 0

def aou(a, b, c, d):
    x, y = 0, 1
    area1 = (b[x]-a[x]) * (b[y]-a[y])
    area2 = (d[x]-c[x]) * (d[y]-c[y])
    intersect = aoi(a, b, c, d)
    return area1 + area2 - intersect

A = (1, 2)
B = (4, 6)
C = (3, 4)
D = (5, 8)
print(aou(A, B, C, D))