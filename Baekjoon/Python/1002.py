import math
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        maxR = max(r1, r2)
        minR = min(r1, r2)
        length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if minR + length < maxR:
            print(0)
        elif minR + length == maxR:
            print(1)
        else:
            if minR + maxR == length:
                print(1)
            elif minR + maxR < length:
                print(0)
            elif minR + maxR > length:
                print(2)
