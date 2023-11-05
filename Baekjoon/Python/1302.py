import sys

n = int(sys.stdin.readline())
map = dict()
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp in map:
        map[tmp] += 1
    else:
        map[tmp] = 1
book = max(map.values())
sell = list()
for key, value in map.items():
    if value == book:
        sell.append(key)
sell = sorted(sell)
print(sell[0])
