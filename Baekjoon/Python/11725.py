from collections import deque

n = int(input())
tree = [[] for _ in range(n)]

for i in range(n - 1):
    n1, n2 = map(int, input().split())
    n1 -= 1
    n2 -= 1
    tree[n1].append(n2)
    tree[n2].append(n1)

visited = [False] * n
parentNode = [0] * n
queue = deque()
queue.append(0)
visited[0] = True

while queue:
    v = queue.popleft()
    for node in tree[v]:
        if not visited[node]:
            visited[node] = True
            queue.append(node)
            parentNode[node] = v

for i in range(1, n):
    print(parentNode[i] + 1)
