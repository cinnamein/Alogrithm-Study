import sys

t = int(sys.stdin.readline())
f = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 101):
    f.append(f[i - 1] + f[i - 5])
for _ in range(t):
    n = int(sys.stdin.readline())
    print(f[n - 1])
