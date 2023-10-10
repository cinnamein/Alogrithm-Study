from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
island = [[] for _ in range(n)]
for i in range(n):
    island[i] = list(sys.stdin.readline().strip())
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]


def bfs(i, ii):
    queue = deque()
    queue.append((i, ii))
    visited = [[0] * m for _ in range(n)]
    visited[i][ii] = 1
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and island[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1


result = 0
for i in range(n):
    for ii in range(m):
        if island[i][ii] == 'L':
            result = max(result, bfs(i, ii))
print(result)
