import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0


def dp(x1, y1, x2, y2, state):
    global result
    if x2 < n and y2 < n:
        if state == 1:
            if house[y2][x2] == 0:
                if x2 == n - 1 and y2 == n - 1:
                    result += 1
                    return
                dp(x2, y2, x2 + 1, y2, 1)
                dp(x2, y2, x2 + 1, y2 + 1, 3)
        elif state == 2:
            if house[y2][x2] == 0:
                if x2 == n - 1 and y2 == n - 1:
                    result += 1
                    return
                dp(x2, y2, x2, y2 + 1, 2)
                dp(x2, y2, x2 + 1, y2 + 1, 3)
        elif state == 3:
            if house[y2][x2] == 0 and house[y1][x2] == 0 and house[y2][x1] == 0:
                if x2 == n - 1 and y2 == n - 1:
                    result += 1
                    return
                dp(x2, y2, x2 + 1, y2, 1)
                dp(x2, y2, x2, y2 + 1, 2)
                dp(x2, y2, x2 + 1, y2 + 1, 3)


if house[n - 1][n - 1] == 1:
    print(0)
else:
    dp(0, 0, 1, 0, 1)
    print(result)
