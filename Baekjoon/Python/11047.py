import sys

n, k = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
res = 0
while True:
    tmp = li.pop()
    res += k // tmp
    k %= tmp
    if k == 0:
        break
print(res)
