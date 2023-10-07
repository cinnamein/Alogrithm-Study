import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
num = 0
for i in arr:
    num += i
if num % m == 0:
    print(1)
else:
    print(0)
