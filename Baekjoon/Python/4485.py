import sys
from collections import deque

input = sys.stdin.readline
movementX = [1, -1, 0, 0]
movementY = [0, 0, 1, -1]


def bfs(x, y, rupee):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + movementX[i]
            my = y + movementY[i]
            if 0 <= mx < n and 0 <= my < n:
                if cost[my][mx] > cost[y][x] + rupee[my][mx]:
                    cost[my][mx] = cost[y][x] + rupee[my][mx]
                    queue.append((mx, my))


num = 0
while True:
    num += 1
    n = int(input())
    if n == 0:
        break
    rupee = [list(map(int, input().split())) for _ in range(n)]
    cost = [[140625 for _ in range(n)] for _ in range(n)]
    cost[0][0] = rupee[0][0]
    bfs(0, 0, rupee)
    print('Problem', num, end='')
    print(':', cost[n - 1][n - 1])
