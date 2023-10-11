import sys

n = int(sys.stdin.readline())
lines = []
count = {}
maxArea = 1
minArea = 1

for _ in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    lines.append((direction, length))
    count[direction] = count.get(direction, 0) + 1

for i in range(6):
    if count[lines[i][0]] == 1:
        maxArea *= lines[i][1]
    if lines[i][0] == lines[(i + 2) % 6][0]:
        minArea *= lines[(i + 1) % 6][1]

result = (maxArea - minArea) * n
print(result)
