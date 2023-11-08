import sys

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    if x2 < x3 or y2 < y3 or x4 < x1 or y4 < y1:
        print('d')
    elif x1 == x4 or x2 == x3:
        if y1 == y4 or y2 == y3:
            print('c')
        else:
            print('b')
    elif y1 == y4 or y2 == y3:
        print('b')
    else:
        print('a')
