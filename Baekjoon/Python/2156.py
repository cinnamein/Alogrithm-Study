import sys

n = int(sys.stdin.readline())
wine = list()
for _ in range(n):
    wine.append(int(sys.stdin.readline()))
result = [0] * n
result[0] = wine[0]
if 1 != n > 0:
    result[1] = wine[1] + wine[0]
for i in range(2, n):
    result[i] = max(wine[i] + wine[i - 1] + result[i - 3], result[i - 1], wine[i] + result[i - 2])
print(result[n - 1])
