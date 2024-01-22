t = int(input())
dp = [1, 1, 2]
for i in range(3, 1000001):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
for _ in range(t):
    print(dp[int(input())])
