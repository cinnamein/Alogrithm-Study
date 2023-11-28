import sys

n = int(sys.stdin.readline())
water = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
toggle = [True for _ in range(n)]
result = sum(water)
print(result)
for _ in range(q):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        a, b = tmp[1], tmp[2]
        before = water[a - 1]
        water[a - 1] = b
        if toggle[a - 1]:
            result = result - before + water[a - 1]
    elif tmp[0] == 2:
        a = tmp[1]
        toggle[a - 1] = not toggle[a - 1]
        if toggle[a - 1]:
            result += water[a - 1]
        else:
            result -= water[a - 1]
    print(result)
