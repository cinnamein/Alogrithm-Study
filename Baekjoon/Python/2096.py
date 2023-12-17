import sys

n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
resultMax = tmp
resultMin = tmp
for _ in range(n - 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    resultMax = [max(resultMax[0], resultMax[1]) + tmp[0], max(resultMax[0], resultMax[1], resultMax[2]) + tmp[1], max(resultMax[1], resultMax[2]) + tmp[2]]
    resultMin = [min(resultMin[0], resultMin[1]) + tmp[0], min(resultMin[0], resultMin[1], resultMin[2]) + tmp[1], min(resultMin[1], resultMin[2]) + tmp[2]]
print(max(resultMax), min(resultMin))
