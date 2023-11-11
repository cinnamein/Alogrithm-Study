import sys

k, n = map(int, sys.stdin.readline().split())
lan = [0] * k
low = 1
high = 2147483647

for i in range(k):
    tmp = int(sys.stdin.readline())
    lan[i] = tmp

while low != high:
    if high == low:
        break
    sum = 0
    mid = (high + low) // 2
    for i in lan:
        sum += i // mid
    if sum >= n:
        low = mid + 1
    elif sum < n:
        high = mid - 1

print(high - 1)
