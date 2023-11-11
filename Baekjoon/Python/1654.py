import sys

k, n = map(int, sys.stdin.readline().split())
lan = [0] * k
low = 0
high = 2147483647
res = 0

for i in range(k):
    tmp = int(sys.stdin.readline())
    lan[i] = tmp

while low <= high:
    mid = (high + low) // 2
    sum = 0
    for i in lan:
        sum += i // mid
    if sum >= n:
        low = mid + 1
        res = mid
    elif sum < n:
        high = mid - 1

print(res)
