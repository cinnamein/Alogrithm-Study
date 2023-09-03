import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

def dp(cnt, num, tmp):
    tmp += str(arr[num]) + ' '
    cnt += 1
    if cnt == m:
        print(tmp)
    else:
        for i in range(num, n):
            dp(cnt, i, tmp)

for i in range(n):
    dp(0, i, '')
