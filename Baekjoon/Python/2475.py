import sys

arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in arr:
    res += i * i
print(res % 10)
