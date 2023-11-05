import sys

n, k = map(int, sys.stdin.readline().split())
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
stuff = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i - 1][0]
        value = stuff[i - 1][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[n][k])
