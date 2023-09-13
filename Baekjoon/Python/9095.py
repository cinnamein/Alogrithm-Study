import sys

n = int(sys.stdin.readline())
dp = [0] * 12
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44
dp[8] = 81
dp[9] = 149
dp[10] = 274
dp[11] = 504
for _ in range(n):
    m = int(sys.stdin.readline())
    print(dp[m])
