import sys
test = int(sys.stdin.readline())

for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    print(n - 1)
    for _ in range (m):
        sys.stdin.readline()