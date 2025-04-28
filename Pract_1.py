# graph = {
#     "5":["3", "7"],
#     "3":["2", "4"],
#     "7":["8"],
#     "2":[],
#     "4":["8"],
#     "8":["2"]
# }

def BFS(graph, node):
    queue = [node]
    visited = [node]

    print("\nOrder of visited nodes by BFS:", end="")

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

def DFS(graph, node):
    stack = [node]
    visited = []
    
    print("\nOrder of visited nodes by DFS:", end="")

    while stack:
        s = stack.pop()
        print(s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)

graph = {}
while True:
    node = input("Enter node (or leave empty to finish): ")
    if not node:
        break
    neighbour = input(f"Enter neighbours for {node}: ").split(",")
    graph[node] = [n.strip() for n in neighbour if n.strip()]

start_node = input("\nEnter the starting node: ") 

BFS(graph, "5")
DFS(graph, "5")
