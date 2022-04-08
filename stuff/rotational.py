N = int(input())
strings = [[input(), input()] for _ in range(N)]

for s, a in strings:
    if len(s) != len(a):
        print("NO")
        continue
    for i in range(len(s)):
        for j in range(i, i+len(a)):
            if s[j%len(s)] != a[j-i]: break
        else:
            print("YES")
            break
    else:
        print("NO")