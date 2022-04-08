N = int(input())

totalSum = 0

def recurse(neighbors, cur, vis, rem):
    global totalSum
    print(rem, cur)
    if len(rem) == 0:
        print("Nothing in rem left")
        return
    for neighbor in neighbors[cur]:
        if not vis[neighbor[0]]:
            if neighbor[0] in rem:
                rem.discard(neighbor[0])
            vis[neighbor[0]] = True
            totalSum += 2*neighbor[1]
            print("visiting", neighbor[0], "from", cur, "with cost", neighbor[1])
            recurse(neighbors, neighbor[0], vis, rem)


for _ in range(N):
    totalSum = 0
    M, K = map(int, input().split(" "))
    deliveryNodes = list(map(int, input().split(" ")))
    neighbors = [set() for _ in range(M+1)]
    # vis = [[0] for _ in range(M+1)] * (M+1)
    vis = [False for _ in range(M+1)]
    for _ in range(M-1):
        ui, vi, ci = map(int, input().split(" "))
        neighbors[ui].add((vi, ci))
        neighbors[vi].add((ui, ci))
    for i in range(len(neighbors)):
        neighbors[i] = list(neighbors[i])
    v = deliveryNodes[0]
    deliveryNodes = set(deliveryNodes)
    deliveryNodes.remove(v)
    recurse(neighbors, v, vis, deliveryNodes)
    print(totalSum)
    
    # print(neighbors)
