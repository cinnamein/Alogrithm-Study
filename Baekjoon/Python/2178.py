import sys

n, m = map(int, sys.stdin.readline().split())
maze = [[0 for _ in range(m)] for _ in range(n)]
for y in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    for x in range(m):
        maze[y][x] = int(tmp[x])
