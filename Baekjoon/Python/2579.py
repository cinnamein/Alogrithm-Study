import sys

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
result = [0] * n
result[0] = stair[0]
if n > 1:
    result[1] = stair[0] + stair[1]
if n > 2:
    result[2] = max(stair[1] + stair[2], stair[0] + stair[2])
    for i in range(3, n):
        result[i] = max(stair[i] + stair[i - 1] + result[i - 3], stair[i] + result[i - 2])
print(result[n - 1])
