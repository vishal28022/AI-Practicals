import sys

def primMST(graph, vertices):
    key = [sys.maxsize] * vertices
    parent = [None] * vertices
    key[0] = 0
    mstSet = [False] * vertices
    parent[0] = -1

    for _ in range(vertices):
        min_key = sys.maxsize
        u = -1
        for v in range(vertices):
            if not mstSet[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        mstSet[u] = True

        for v in range(vertices):
            if graph[u][v] and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("\nPrim's MST:")
    total_weight = 0
    print("Edge \tWeight")
    for i in range(1, vertices):
        print(parent[i], "-", i, "\t", graph[parent[i]][i])
        total_weight += graph[parent[i]][i]
    print("Total weight of MST:", total_weight)

# ------------------------------------------------
# ✅ Very Simple Version of Kruskal’s Algorithm:

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskalMST(edges, vertices):
    edges.sort()
    parent = [i for i in range(vertices)]
    rank = [0] * vertices
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst.append((u, v, weight))
            union(parent, rank, x, y)
            total_weight += weight

    print("\nKruskal's MST:")
    print("Edge \tWeight")
    for u, v, weight in mst:
        print(u, "-", v, "\t", weight)
    print("Total weight of MST:", total_weight)

# ------------------------------------------------
# Main Program:

vertices = int(input("Enter the number of vertices: "))
graph = []

print("\nEnter the adjacency matrix (use 0 if no edge exists):")
for i in range(vertices):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    if len(row) != vertices:
        print("Error: Please enter exactly", vertices, "numbers.")
        sys.exit(1)
    graph.append(row)

# Building the list of edges for Kruskal
edges = []
for i in range(vertices):
    for j in range(i, vertices):
        if graph[i][j] != 0:
            edges.append((graph[i][j], i, j))

primMST(graph, vertices)
kruskalMST(edges, vertices)
