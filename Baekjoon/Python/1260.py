n, m, v = map(int, input().split())
arr = [[False] * (n + 1) for _ in range(n + 1)]
check = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = True
    arr[b][a] = True

def bfs(v):
    check = [False] * (n + 1)
    list = [v]
    check[v] = True
    while list:
        v = list.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            if arr[v][i] and not check[i]:
                list.append(i)
                check[i] = True

def dfs(v):
    check[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if arr[v][i] and not check[i]:
            dfs_stack.append(i)
            check[i] = True
            dfs(i)

check = [False] * (n + 1)
dfs_stack = []
dfs(v)
print()
check = [False] * (n + 1)
bfs(v)
