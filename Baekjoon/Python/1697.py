from collections import deque

n, k = map(int, input().split())
visit = [0] * 100001

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 1

    while queue:
        tmp = queue.popleft()

        if tmp == k:
            return visit[tmp] - 1

        if tmp - 1 >= 0 and visit[tmp - 1] == 0:
            visit[tmp - 1] = visit[tmp] + 1
            queue.append(tmp - 1)

        if tmp + 1 < 100001 and visit[tmp + 1] == 0:
            visit[tmp + 1] = visit[tmp] + 1
            queue.append(tmp + 1)

        if tmp * 2 < 100001 and visit[tmp * 2] == 0:
            visit[tmp * 2] = visit[tmp] + 1
            queue.append(tmp * 2)

    return -1

if n == k:
    print(0)
else:
    print(bfs(n))
