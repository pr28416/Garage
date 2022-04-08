N = int(input())
for _ in range(N):
    key = input().split(" ")
    message = input().split(" ")
    mp = {}
    for i in range(0, len(key)-1, 2):
        mp[key[i+1]] = key[i]
    print("".join(map(lambda x: mp[x], message)))