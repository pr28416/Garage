def sumOfLastRow(s, d, r):
    s = int("0o" + str(s), 8)
    d = int("0o" + str(d), 8)
    n = (r - 1) * r // 2 + 1

    fin = 0
    for i in range(n, n + r):
        a = oct(s + d * (i - 1))
        for j in range(2, len(a)):
            fin += int(a[j])
    return fin