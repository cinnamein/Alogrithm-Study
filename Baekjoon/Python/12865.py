import sys

n, m = map(int, sys.stdin.readline().split())
arr = (map(int, sys.stdin.readline().split()) for _ in range(n))
res = 0

def dp(num, cnt, w, cost):
    tmpW = w + arr[num][0]
    tmpCost = cost + arr[num][1]
    if tmpW >= m:
        return
    else:
        dp(num, cnt, tmpW, tmpCost)
    global res
    res = max(tmpCost, res)

for i in range(n):
    # 스타트
    for ii in range(n):
        # 몇 개
        dp(i, ii, 0, 0)
print(res)
