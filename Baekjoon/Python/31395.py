n = int(input())
li = list(map(int, input().split()))
result = 0
cnt = 1

for i in range(1, n):
    if li[i - 1] <= li[i]:
        cnt += 1
    else:
        result += cnt * (cnt + 1) // 2
        cnt = 1
result += cnt * (cnt + 1) // 2
print(result)
