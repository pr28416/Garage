from math import inf

with open("Djikstra_input0.txt") as f:
    N, S = map(int, f.readline().split(" "))
    graph = [[inf] * N for i in range(N)]
    for line in f.readlines():
        u, v, c = map(int, line.split(" "))

        graph[u][v] = min(c, graph[u][v])
        graph[v][u] = min(c, graph[v][u])

for u in range(len(graph)):
    for v in range(len(graph[u])):
        if graph[u][v] != inf:
            print(f"({u},{v},{graph[u][v]})")

shortestPathCosts, remaining = [inf] * N, {i for i in range(N) if i != S}
shortestPathCosts[S] = 0
lastVertex = S

for _ in range(N-1):
    v = None
    for u in remaining:
        if v is None: v = u
        if graph[lastVertex][u] == inf: continue
        shortestPathCosts[u] = min(shortestPathCosts[u], shortestPathCosts[lastVertex] + graph[lastVertex][u])
        if shortestPathCosts[u] < shortestPathCosts[v]:
            v = u
    print(v, shortestPathCosts, remaining)
    remaining.remove(v)
    lastVertex = v

print(shortestPathCosts)