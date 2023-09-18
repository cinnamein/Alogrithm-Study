import sys

li = []
n = int(sys.stdin.readline())
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    if tmp == '0':
        li.pop()
    else:
        li.append(tmp)
res = 0
for i in li:
    res += int(i)
print(res)
