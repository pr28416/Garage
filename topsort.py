def dfs_search(G, v, visited, postorder):
    for w in G[v]:
        if not visited[w]:
            visited[w] = True
            dfs_search(G, w, visited, postorder)
    postorder.append(v)

def topsort(G):
    visited = [False] * len(G)
    postorder = []
    for v in range(len(G)):
        if not visited[v]:
            dfs_search(G, v, visited, postorder)
    return postorder[::-1]

res = topsort([
    [1, 2, 3],
    [4],
    [5, 7],
    [5, 6],
    [8],
    [7],
    [7],
    [8],
    [],
])

print(res)

"""
    +----> 1 ----> 4 ----+
    |                    v
0 --> 2 ----> 5 ----> 7 --> 8
    |       ^         ^
    +----> 3 ----> 6 --+
"""