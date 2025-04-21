import sys 

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.edges = []

    def add_edges_from_adj_matrix(self):
        for i in range(self.v):
            for j in range(i, self.v):
                if self.graph[i][j] != 0:
                    self.edges.append((self.graph[i][j], i, j))
        
# ----------------- Prim's Algorithm -------------------
    def print_prim_MST(self, parent):
        print("Prim's MST:")
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
            total_weight += self.graph[parent[i]][i]
        print("Total weight of MST: ", total_weight)

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.v):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index
    
    def primMST(self):
        key = [sys.maxsize] * self.v
        parent = [None] * self.v
        key[0] = 0 
        mstSet = [False] * self.v
        parent[0] = -1

        for cout in range(self.v):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_prim_MST(parent)

# ------------------ Kruskal's Algorithm ---------------------
    def find (self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot 
            rank[xroot] += 1

    def kruskalMST(self):
        self.edges.sort()
        parent = [i for i in range(self.v)]
        rank = [0] * self.v

        mst = []
        total_weight = 0
        
        for weight, u, v, in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                mst.append((u, v, weight))
                self.union(parent, rank, x, y)
                total_weight += weight

        print("Kruskal's MST:")
        print("Edge \t Weight")
        for u, v, weight in mst:
            print(u, "-", v, "\t", weight)
        print("Total weight of MST:", total_weight)

# --------------- Main function ---------------
if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    print("\nEnter the adjacency matrix (use 0 if no edge exists):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != vertices:
            print("Error: Please enter exactly", vertices, "numbers.")
            sys.exit(1)
        g.graph[i] = row

    g.add_edges_from_adj_matrix()

    print("\nRunning Prim's Algorithm...")
    g.primMST()

    print("\nRunning Kruskal's Algorithm...")
    g.kruskalMST()