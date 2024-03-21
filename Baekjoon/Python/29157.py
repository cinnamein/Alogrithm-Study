n, m, k = map(int, input().split())
li = [[False for _ in range(n + 1)] for _ in range(m + 1)]
liSum = [[1 for _ in range(n + 1)] for _ in range(m + 1)]
visit = [[False for _ in range(n + 1)] for _ in range(m + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    li[y][x] = True
    liSum[y][x] = 0
result = 0
nextCase = list()
nextCase.append([1, 1])


def bfs(x, y):
    visit[y][x] = True
    nextCase.append([y + 1, x])
    nextCase.append([y, x + 1])
    if not li[y][x]:
        liSum[y][x] = (liSum[y - 1][x] + liSum[y][x - 1]) % 1000000007


for tmp in nextCase:
    a, b = tmp[0], tmp[1]
    if 0 < a <= n and 0 < b <= m and not visit[b][a]:
        bfs(a, b)
print(liSum[m][n])
