import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
low = 0
high = 1000000000
res = 0

while low <= high:
    sum = 0
    mid = (low + high) // 2
    for i in tree:
        tmp = i - mid
        if tmp > 0:
            sum += tmp
    if sum >= m:
        res = mid
        low = mid + 1
    elif sum < m:
        high = mid - 1

print(res)
