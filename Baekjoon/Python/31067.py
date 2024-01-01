n, k = map(int, input().split())
track = list(map(int, input().split()))
result = 0
for i in range(1, n):
    if track[i] > track[i - 1]:
        continue
    else:
        if track[i] + k > track[i - 1]:
            track[i] += k
            result += 1
            continue
        else:
            result = -1
            break
print(result)
