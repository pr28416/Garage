N = int(input())
for _ in range(N):
    key = input().split(" ")
    message = input()
    mp = {}
    for i in range(0, len(key)-1, 2):
        mp[key[i+1]] = key[i]
    lo = 0
    res = ""
    for up in range(1, len(message)+1):
        v = message[lo:up]
        if v in mp:
            res += mp[v]
            lo = up
    print(res)

    # print("".join(map(lambda x: mp[x], message)))