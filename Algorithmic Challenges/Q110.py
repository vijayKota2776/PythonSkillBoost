from collections import deque
def is_valid_move(x, y, m, n, visited):
    return 0 <= x < m and 0 <= y < n and not visited[x][y]
def bfs_shortest_path(grid):
    m = len(grid)
    n = len(grid[0])
    directions = [(0, 1), (1, 0)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = deque([(0, 0, 0)])  
    visited[0][0] = True
    while queue:
        x, y, dist = queue.popleft()
        if x == m - 1 and y == n - 1:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, m, n, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1)) 
    return -1
grid = [
    [1, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]
shortest_path = bfs_shortest_path(grid)
if shortest_path != -1:
    print(f"The shortest path length is: {shortest_path}")
else:
    print("No valid path exists.")
