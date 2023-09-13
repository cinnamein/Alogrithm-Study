import sys

n, m = map(int, sys.stdin.readline().split())
a, b = 1, 1
for i in range(1, m + 1):
    a *= n - i + 1
    b *= i
print(a // b)
