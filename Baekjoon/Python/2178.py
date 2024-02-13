import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque()
maze = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def movement(x, y, cnt):
    global maze, visited
    if not (0 <= x < m) or not (0 <= y < n) or visited[y][x] or maze[y][x] == 0:
        return
    maze[y][x] = cnt
    visited[y][x] = True
    global queue
    queue.append([x - 1, y, cnt + 1])
    queue.append([x + 1, y, cnt + 1])
    queue.append([x, y - 1, cnt + 1])
    queue.append([x, y + 1, cnt + 1])


for y in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    for x in range(m):
        maze[y][x] = int(tmp[x])
queue.append([0, 0, 1])
while True:
    if len(queue) == 0:
        break
    tmp = queue.popleft()
    movement(tmp[0], tmp[1], tmp[2])
print(maze[n - 1][m - 1])
