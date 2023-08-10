import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(li)):
    li[i] = li[i] + li[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(li[j - 1])
    else:
        print(li[j - 1] - li[i - 2])
