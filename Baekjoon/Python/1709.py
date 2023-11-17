n = int(input())
x, y, r, cnt = 0, n // 2 - 1, (n // 2) ** 2, 0
while x <= n // 2 and y >= 0:
    distance = (x + 1) * (x + 1) + y * y
    if distance <= r:
        x += 1
    if distance >= r:
        y -= 1
    cnt += 1
print(cnt * 4)
