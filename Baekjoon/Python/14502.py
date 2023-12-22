from collections import deque
import copy
import sys

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
movementX = [-1, 1, 0, 0]
movementY = [0, 0, -1, 1]


def bfs():
    queue = deque()
    graphTmp = copy.deepcopy(graph)
    for i in range(n):
        for k in range(m):
            if graphTmp[i][k] == 2:
                queue.append((i, k))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            dr = r + movementY[i]
            dc = c + movementX[i]
            if (0 <= dr < n) and (0 <= dc < m):
                if graphTmp[dr][dc] == 0:
                    graphTmp[dr][dc] = 2
                    queue.append((dr, dc))

    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if graphTmp[i][k] == 0:
                count += 1
    result = max(result, count)


def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if graph[i][k] == 0:
                graph[i][k] = 1
                wall(count + 1)
                graph[i][k] = 0


result = 0
wall(0)
print(result)
