import heapq # Used to get smallest edge from each vertex

mst = [] # Maintains edges in MST
usedVertices = set() # Maintains used vertices
with open("PrimMST_inputs/PrimMST_input3.txt") as f:
    numVertices = int(f.readline())
    edges = [[] for _ in range(numVertices)]
    for line in f.readlines():
        edge = tuple(map(int, line.split(" ")))
        # Check if self loop - no self loops allowed
        if edge[0] == edge[1]: continue
        # 0, 1: vertices, 2: edge
        heapq.heappush(edges[edge[0]], (edge[2], edge[1]))
        heapq.heappush(edges[edge[1]], (edge[2], edge[0]))

# Print for reference
# for i, edge in enumerate(edges):
#     print(i, ": ", edge, sep="")

cost, dest = 0, 1
# Keep iterating until all vertices are used
while len(usedVertices) < numVertices:
    vertexWithSmallestEdge = 0
    # Iterate through all vertices
    for vertex in usedVertices:
        # Remove any edges between two used vertices
        while len(edges[vertex]) > 0 and edges[vertex][0][dest] in usedVertices:
            heapq.heappop(edges[vertex])

        # If there are no edges from the vertex, continue
        if len(edges[vertex]) == 0: continue

        # Conditions:
        # - All edges from vertexWithSmallestEdge are used OR
        # - New edge cost < current vertexWithSmallestEdge cost
        if len(edges[vertexWithSmallestEdge]) == 0 or edges[vertex][0][cost] < edges[vertexWithSmallestEdge][0][cost]:
            vertexWithSmallestEdge = vertex
    
    # Using newly found vertex:
    # - Add edge to MST
    # - Add both vertices of edge to usedVertices
    edge = heapq.heappop(edges[vertexWithSmallestEdge])
    mst.append((vertexWithSmallestEdge, edge[dest], edge[cost]))
    usedVertices.add(vertexWithSmallestEdge)
    usedVertices.add(edge[dest])

# Print MST
print(mst)