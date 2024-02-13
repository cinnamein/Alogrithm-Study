h, w = map(int, input().split())
r, c, d = map(int, input().split())
result = 0
visited = [[False for _ in range(w)] for _ in range(h)]
ruleA = list(list(input()) for _ in range(h))
ruleB = list(list(input()) for _ in range(h))
while True:
    if not visited[r][c]:
        visited[r][c] = True
        cleaning = True
print(result)
