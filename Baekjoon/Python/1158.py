from collections import deque

n, m = map(int, input().split())
tmp = deque()
for i in range(1, n + 1):
    tmp.append(i)
res = [] * n
while tmp:
    for _ in range(m - 1):
        tmp.append(tmp.popleft())
    res.append(tmp.popleft())
print(str(res).replace('[', '<').replace(']', '>'))
