import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
friend = [deque() for _ in range(n)]
visited = [False for _ in range(n)]
res = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)


def dfs(person, depth):
    if visited[person]:
        return
    visited[person] = True
    if depth == 5:
        global res
        res = 1
        return
    for i in friend[person]:
        dfs(i, depth + 1)
    visited[person] = False


for i in range(n):
    dfs(i, 1)
print(res)
