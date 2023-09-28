import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
input_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result_arr = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
qu = deque()
mx, my = [-1, 1, 0, 0], [0, 0, -1, 1]

# 2 찾기
for i in range(n):
    for ii in range(m):
        if input_arr[i][ii] == 2:
            startX = ii
            startY = i
        elif input_arr[i][ii] == 0:
            result_arr[i][ii] = 0
            visited[i][ii] = True


def bfs(curX, curY):
    # 다음 이동 칸
    for i in range(4):
        nextX = curX + mx[i]
        nextY = curY + my[i]
        # 방문하지 않은 칸이고, 범위 안의 좌표일 때만 실행
        if 0 <= nextX < m and 0 <= nextY < n and not visited[nextY][nextX]:
            result_arr[nextY][nextX] = result_arr[curY][curX] + 1
            visited[nextY][nextX] = True
            qu.append([nextX, nextY])


result_arr[startY][startX] = 0
visited[startY][startX] = True
qu.append([startX, startY])
while len(qu) != 0:
    tmp = qu.popleft()
    bfs(tmp[0], tmp[1])

for i in range(n):
    for ii in range(m):
        print(result_arr[i][ii], end=' ')
    print()
