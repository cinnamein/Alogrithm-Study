import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
les = cost[0]

for i in range(n - 1):
    les = min(les, cost[i])
    res += les * distance[i]
print(res)
