import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = [[-1] * m] * n
vis = [[False] * m] * n
a, b = 0, 0
mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]
for y in range(n):
    for x in range(m):
        if arr[y][x] == 2:
            a = x
            b = y
vis[b][a] = True


def bfs(tmpx, tmpy):
    for i in range(4):
        y = tmpy + my[i]
        x = tmpx + mx[i]
        if 0 <= y < n and 0 <= x < m:
            if arr[y][x] == 0:
                res[y][x] = 0
                return
            elif res[y][x] == -1:
                res[y - 1][x] = res[y][x] + 1
    for i in range(4):
        bfs(tmpx + mx[i], tmpy + my[i])


bfs(a, b)
print(res)
