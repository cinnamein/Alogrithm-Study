import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
sum = li.copy()
cnt = 0
for i in range(1, n):
    sum[i] += sum[i - 1]
for k in range(n):
    if sum[k] == m:
        cnt += 1
    for kk in range(k):
        tmp = sum[k] - sum[kk]
        if tmp == m:
            cnt += 1
print(cnt)
