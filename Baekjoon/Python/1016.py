import math

n, m = map(int, input().split())
arr = list()
result = m - n + 1

tmp = int(math.sqrt(m) + 1)

for i in range(2, tmp):
    arr.append(i * i)

for k in range(n, m + 1):
    if any(k % prime == 0 for prime in arr):
        result -= 1

print(result)
