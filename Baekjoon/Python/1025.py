n, m = map(int, input().split())
a = int(input())
b = int(input())
arr = [list(input().split()) for _ in range(n)]
result = -1

for i in range(n):
    for ii in range(m):
        for x in range(-n, n):
            for y in range(-m, m):
                if x == 0 and y == 0:
                    continue
                tmp = ""
                x, y = i, ii
                while 0 <= x <= n and 0 <= y <= m:
                    tmp += arr[y][x]
                    if int(int(tmp) ** 0.5) ** 2 == int(tmp):
                        result = max(int(tmp), result)
                    x += i
                    y += ii
print(result)