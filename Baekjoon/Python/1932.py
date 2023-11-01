import sys

n = int(sys.stdin.readline())
tree = [list()] * n
for i in range(n):
    tree[i] = list(map(int, sys.stdin.readline().split()))

for y in range(1, n):
    for x in range(y + 1):
        if x == 0:
            tree[y][x] += tree[y - 1][x]
        elif x == y:
            tree[y][x] += tree[y - 1][x - 1]
        else:
            tree[y][x] += max(tree[y - 1][x - 1], tree[y - 1][x])

print(max(tree[n - 1]))
