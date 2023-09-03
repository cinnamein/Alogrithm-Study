import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visit = [False] * n


def dp(num, li, res, cnt):
    res += str(arr[num]) + ' '
    li[num] = True
    cnt += 1
    if cnt == m:
        print(res)
        return
    for i in range(n):
        if not li[i]:
            dp(i, li[:], res, cnt)


for k in range(n):
    dp(k, [False] * n, '', 0)
