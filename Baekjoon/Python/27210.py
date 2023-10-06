import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arrSum = [0] * n
maxSum, minSum, tmp, res = 0, 0, 0, 0
for i in arr:
    if i == 1:
        tmp += 1
    elif i == 2:
        tmp -= 1
    res = max(res, abs(tmp - minSum))
    res = max(res, abs(maxSum - tmp))
    maxSum = max(maxSum, tmp)
    minSum = min(minSum, tmp)
print(res)
