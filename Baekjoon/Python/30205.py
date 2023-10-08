import sys

n, m, p = map(int, sys.stdin.readline().split())
floor = list()
for i in range(n):
    floor.append(sorted(list(map(int, sys.stdin.readline().split()))))
flag = 1
for k in range(n):
    powerCnt = 0
    for kk in range(m):
        tmp = floor[k][kk]
        if tmp == -1:
            powerCnt += 1
        elif tmp > p:
            while True:
                powerCnt -= 1
                if powerCnt < 0:
                    flag = 0
                    break
                p *= 2
                if p >= tmp:
                    p += tmp
                    break
        elif tmp <= p:
            p += tmp
        if flag == 0:
            break
    for r in range(powerCnt):
        p *= 2
    if flag == 0:
        break
print(flag)
