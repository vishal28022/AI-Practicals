import heapq 

def heuristic(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_list = [(0 + heuristic(start, goal), start)]
    g_score = {start: 0}
    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                new_g = g_score[current] + 1

                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    f_score = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current

    return None

n, m = map(int, input("Grid size(n m): ").split())
grid = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(n)]
start = tuple(map(int, input("Start (row col): ").split())) 
goal = tuple(map(int, input("Goal (row col): ").split()))

path = a_star(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")